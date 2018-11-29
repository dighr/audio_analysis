# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import speech
from google.cloud.speech import enums as speech_enums

from google.cloud.speech import types as speech_types
from google.protobuf.json_format import MessageToJson

import json
import io

from text_analysis.beans import ErrorBean


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
