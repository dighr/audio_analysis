# Imports the Google Cloud client library
import binascii
import io
import json
import os
import tempfile
from multiprocessing.dummy import Pool

import speech_recognition as sr
from google.cloud import language
from google.cloud import speech
from google.cloud import translate
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud.speech import enums as speech_enums
from google.cloud.speech import types as speech_types
from google.protobuf.json_format import MessageToJson
from pydub import AudioSegment

from transcription_analysis.beans import ErrorBean, ResponseBean

audio_directory_path = os.path.join('.', 'audio_files')
tmp_path = os.path.join('.', 'tmp')

# given a text and a method, retreive the sentiment of that text using method modal
def handle_text_analysis_request(text, language_code,  method):

    global value
    if (text is not None) and (method is not None) and (language_code is not None):
        if method == "google":
            try:
                text_to_analyze = text

                if str(language_code).lower() != 'en':
                    translated_text_obj = translate_text_from(text, language_code)
                    text_to_analyze = translated_text_obj['translation']

                text_analysis = get_text_sentiment_values(text_to_analyze)

                response = {
                    'text': text,
                    'language_code': language_code,
                    'translation': text_to_analyze,
                    'text_analysis': json.loads(text_analysis)
                }

                text_bean = ResponseBean(response)
                value = json.dumps(text_bean.__dict__)
            except Exception as e:
                value = get_error_message(str(e))
        else:
            value = get_error_message("The method specified is not supported")
    else:
        value = get_error_message("'text' or 'method' or 'source_language' were not passed in the argument")

    return value


def handle_translation_request(text, language_code):
    global value
    if (language_code is not None) and (text is not None):

        try:
            resp = translate_text_from(text, str(language_code).split("-")[0])
            translation_bean = ResponseBean(resp)
            value = json.dumps(translation_bean.__dict__)
        except Exception as e:
            value = get_error_message(str(e))
    else:
        value = get_error_message("'text' and 'language_code' were not passed in the argument")

    return value


# given a file on instance of UploadedFile, transcribe and analyze the audio
def handle_audio_analysis_request(file_obj, language_code="en-US"):
    try:
        # Transcribe
        text = transcribe_any_audio(file_obj, language_code)

        # translate the text if language_code is not english
        iso = str(language_code).split("-")[0]
        translation = text
        if iso.lower() != 'en':
            translation = translate_text_from(text, iso.lower())['translation']

        # Do a sentiment analysis on the transcribed text
        text_analysis = get_text_sentiment_values(translation)

        # return the answers in a JSON format
        response = {
            'audio_text': text,
            'translation': translation,
            'audio_analysis':  json.loads(text_analysis)
        }

        # Create an success bean object
        audio_bean = ResponseBean(response)

        # return the response as json
        return json.dumps(audio_bean.__dict__)

    except Exception as e:
        return get_error_message(str(e))


# given a file on instance of UploadedFile, transcribe the audio
def handle_audio_transcription_request(file_obj, language_code="en-US"):
    try:
        # Get the transcribed text
        text = transcribe_any_audio(file_obj, language_code)

        # translate the text if language_code is not english
        iso = str(language_code).split("-")[0]
        translation = text
        if iso.lower() != 'en':
            translation = translate_text_from(text, iso.lower())['translation']

        # return the answer in a JSON format
        response = {
            'file_name': file_obj.name,
            'audio_text': text,
            'translation': translation,
        }

        audio_text_bean = ResponseBean(response)
        return json.dumps(audio_text_bean.__dict__)
    except Exception as e:
        return get_error_message(str(e))


def transcribe_any_audio(file_obj, language_code, type="google"):
    file_name = convert_audio_to_wav(file_obj)
    if file_name is None:
        raise Exception("File was not provided or the provided file is not in the following"
                        " format (WAV, MP3, OGG)")

    # Get the duration of the audio file
    if type == "google":
        sound = AudioSegment.from_wav(file_name)
        duration = sound.duration_seconds

        # Based on the duration, transcribe the audio files
        if duration < 60:
            text = transcribe_short_audio(file_name, language_code=language_code)
        else:
            text = transcribe_audio_fast(file_name, language_code=language_code)
    elif type == "deepspeech":
        from transcription_analysis import deepspeech
        ds = deepspeech.DeepSpeech()
        text = ds.transcribe(file_name)
    elif type == "watson":
        from transcription_analysis.watson_transcription import WatsonTranscription
        wt = WatsonTranscription("ZvC-ea0NHkQzZbDUDpSK7ygIBqUa5oCsO_CPQp3yrMzi",
                                 "https://stream.watsonplatform.net/speech-to-text/api")
        text = wt.transcribe(file_name)

    elif type == "azure":
        from transcription_analysis.azure_transcription import AzurTranscription
        at = AzurTranscription("f4e4545e16564863beb1efea6a673e7f", lang=language_code)
        text = at.transcribe(file_name)
    # Remove file_name
    os.remove(file_name)
    return text



# Convert the uploaded audio file to wav if they are not and store them under the audio files folder
def convert_audio_to_wav(file, audio_directory=audio_directory_path, add_id=True):
    if file is None:
        return

    if type(file) == str:
        file_name = str(file).split("/")[-1]
        tempfn = file
    else:
        file_name = file.name
        tempf, tempfn = tempfile.mkstemp()
        for chunk in file.chunks():
                os.write(tempf, chunk)
        os.close(tempf)

    id = ""
    if add_id:
        id = str(binascii.hexlify(os.urandom(32)).decode())
    file_path = os.path.join(audio_directory, os.path.splitext(file_name)[0] + id + ".wav")
    # Encoding Audio file into Wav
    if file_name.endswith('.mp3'):
        sound = AudioSegment.from_mp3(tempfn)
        out = sound.export(file_path, format="wav")
        out.close()
    elif file_name.endswith('.ogg'):
        sound = AudioSegment.from_ogg(tempfn)
        out = sound.export(file_path, format="wav")
        out.close()
    elif file_name.endswith('.wav'):
        sound = AudioSegment.from_wav(tempfn)
        out = sound.export(file_path, format="wav")
        out.close()
    return file_path
    # except:
    #     raise Exception("Problem with the input file %s" % file.name)


# trascribe audios less than one minute with wav format
def transcribe_short_audio(file_path, language_code):
    # Instantiates a client
    client = speech.SpeechClient()

    # Loads the audio into memory
    with io.open(file_path, 'rb') as audio_file:
        # encode
        content = encode_audio(audio_file)
        audio = speech_types.RecognitionAudio(content=content)

    config = speech_types.RecognitionConfig(
        encoding=speech_enums.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code=language_code)

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    text = ""
    for result in response.results:
        text += result.alternatives[0].transcript

    return text


# Transcribe audio with any length, the way this is done is by first, dividing the audio file into smalled chucks
# of 45 seconds, each chuck is transcribed in a separate thread and then assembled in an ordered way at the end
def transcribe_audio_fast(file_path, language_code, name="tmp"):
    # Since tmp_file is required, create it if it does not exist
    if not os.path.exists(tmp_path):
        os.makedirs(tmp_path)

    # Open google APPLICATION CREDENTIALS which is stored in the enviroment variables
    with open(os.environ["GOOGLE_APPLICATION_CREDENTIALS"]) as f:
        GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()

    sound = AudioSegment.from_wav(file_path)

    r = sr.Recognizer()

    # initialize data
    data = []

    # Calculate the voice chucks in miliseconds in the following format (chuck_begin, chuck_end)
    # Append this into the data list
    duration = sound.duration_seconds * 1000
    interval = 58 * 1000
    begin = 0
    if interval < duration:
        end = interval
    else:
        end = duration

    while duration > 0:
        data.append((begin, end))

        # update
        duration -= interval
        begin = end
        if duration < interval:
            end = (end + duration)
        else:
            end = (end + interval)

    # This inner method will be run in a separate thread
    def transcribe(input):
        idx, value = input
        # Retreive the chunck from the audio and store it in the tmp file with a unique name
        sound_interval = sound[value[0]:value[1]]
        audio_segment_path = os.path.join(tmp_path, name + str(binascii.hexlify(os.urandom(32)).decode()) + ".wav")

        out = sound_interval.export(audio_segment_path, format="wav")

        # with sr.AudioFile(audio_segment_path) as source:
        #     audio = r.record(source)

        # Transcribe audio file
        try:
            # text = r.recognize_google_cloud(audio, language=language_code, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
            text = transcribe_short_audio(audio_segment_path, language_code)
        except sr.UnknownValueError:
            text = "*********sub audio was not understood*********"

        # Clear
        os.remove(audio_segment_path)
        out.close()

        return {
            "idx": idx,
            "text": text
        }

    pool = Pool(20)
    all_text = pool.map(transcribe, enumerate(data))
    pool.close()
    pool.join()

    transcript = ""
    for t in sorted(all_text, key=lambda x: x['idx']):
        # Format time as h:m:s - 30 seconds of text
        transcript += t['text']

    return transcript


def translate_text_from(text, source_language, target_language="en"):
    client = translate.Client()
    translation = client.translate(text,
                                   source_language=source_language, target_language=target_language)
    response = {
        'source_language': source_language,
        'text': text,
        'translation': translation['translatedText'],
    }

    return response


def get_text_sentiment_values(text):
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    features = {
        "extract_entities": True,
        "extract_document_sentiment": True,
        "extract_entity_sentiment": True,
    }

    result = client.annotate_text(document=document, features=features)

    return MessageToJson(result)


def get_error_message(error):
    error_obj = ErrorBean(error)
    return json.dumps(error_obj.__dict__)


# Encode the audio function
def encode_audio(audio):
    audio_content = audio.read()
    # return base64.b64encode(audio_content)
    return audio_content
