import binascii
import json
import os
import tempfile
import wave

from google.protobuf.json_format import MessageToJson
from pydub import AudioSegment
from transcription_analysis.beans import ErrorBean, ResponseBean
from transcription_analysis.google_transcription import translate_text_from
from transcription_analysis.google_transcription import get_text_sentiment_values
from google.cloud import storage

audio_directory_path = os.path.join('.', 'audio_files')
bucketname = "dighr_bucket" #Name of the bucket created


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

                text_analysis = MessageToJson(get_text_sentiment_values(text_to_analyze))

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
        text = transcribe_any_audio(file_obj, language_code,  type="google")

        # translate the text if language_code is not english
        iso = str(language_code).split("-")[0]
        translation = text
        if iso.lower() != 'en':
            translation = translate_text_from(text, iso.lower())['translation']

        # Do a sentiment analysis on the transcribed text
        text_analysis = MessageToJson(get_text_sentiment_values(translation))

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
        text = transcribe_any_audio(file_obj, language_code, type="google")

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


def stereo_to_mono(audio_file_name):
    sound = AudioSegment.from_wav(audio_file_name)
    sound = sound.set_channels(1)
    sound.export(audio_file_name, format="wav")


def frame_rate_channel(audio_file_name):
    with wave.open(audio_file_name, "rb") as wave_file:
        frame_rate = wave_file.getframerate()
        channels = wave_file.getnchannels()
        return frame_rate,channels


def upload_audio_file(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)


def delete_audio_files(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.delete()


def transcribe_any_audio(file_obj, language_code, type):
    # convert the given file into a supported file
    file_name = convert_audio_to_wav(file_obj)
    if file_name is None:
        raise Exception("File was not provided or the provided file is not in the following"
                        " format (WAV, MP3, OGG)")

    frame_rate, channels = frame_rate_channel(file_name)
    
    if channels > 1:
        stereo_to_mono(file_name)
    
    bucket_name = bucketname
    source_file_name = file_name
    destination_file_name = file_name
    
    upload_audio_file(bucket_name, source_file_name, destination_file_name)
    
    gcs_uri = 'gs://' + bucket_name + '/' + file_name

    text = None
    if type == "google":
        from transcription_analysis.google_transcription import GoogleTranscription
        gt = GoogleTranscription(language_code)
        text = gt.transcribe(gcs_uri, file_name)
        
    delete_audio_files(bucket_name, destination_file_name)
    # Remove file_name
    os.remove(file_name)

    return text


def get_error_message(error):
    error_obj = ErrorBean(error)
    return json.dumps(error_obj.__dict__)


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
    elif file_name.endswith(".flac"):
        # sound = AudioSegment.from_mp3(tempfn)
        os.system("sox " + tempfn + " " + file_path)
        # out = sound.export(file_path, format="wav")
        # out.close()

    return file_path

