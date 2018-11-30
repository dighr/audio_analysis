# Imports the Google Cloud client library
import json
import io

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import speech
from google.cloud.speech import enums as speech_enums
from google.cloud.speech import types as speech_types
from google.protobuf.json_format import MessageToJson

from transcription_analysis.beans import ErrorBean, AnalyzedAudioBean
from transcription_analysis.serializers import FileSerializer


def handle_audio_analysis_request(request_data):
    file_serializer = FileSerializer(data=request_data)
    # Check for validity
    if file_serializer.is_valid():
        # save the file
        file_serializer.save()
        # get file name
        try:
            file_name = file_serializer.data['file']
            # Get both the transcription and the analysis
            text = transcribe_short_audio(file_name)
            resp = get_text_sentiment_values(text)
            audio_bean = AnalyzedAudioBean(audio_text=text, audio_analysis=resp)
            resp = json.dumps(audio_bean.__dict__)
            return resp
        except Exception as e:
            return get_error_message(str(e))
    else:
        return file_serializer.errors


def handle_text_analysis_request(text, method):
    global value
    if (text is not None) and (method is not None):
        if method == "google":
            try:
                value = get_text_sentiment_values(text)
            except Exception as e:
                get_error_message(str(e))
        else:
            value = get_error_message("The method specified is not supported")
    else:
        value = get_error_message("'text' and 'method' were not passed in the argument")

    return value


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


# for audios less than one minute
def transcribe_short_audio(file_path):
    # Instantiates a client
    client = speech.SpeechClient()

    # Loads the audio into memory
    with io.open(file_path, 'rb') as audio_file:
        content = audio_file.read()
        audio = speech_types.RecognitionAudio(content=content)

    config = speech_types.RecognitionConfig(
        encoding=speech_enums.RecognitionConfig.AudioEncoding.LINEAR16,
        enable_automatic_punctuation=True,
        language_code='en-US')

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    text = ""
    for result in response.results:
        text += result.alternatives[0].transcript

    return text


