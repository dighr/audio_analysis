
# This class acts a bean. Required to convert a python object into json
import json


class AnalyzedTextBean(object):
    def __init__(self, text="", entities="", document_sentiment="", language="en"):
        self.text = text
        self.language = language
        self.entities = entities
        self.document_sentiment = document_sentiment


class AnalyzedAudioBean(object):
    def __init__(self, audio_text="", audio_analysis="{}"):
        self.status = 1
        self.audio_text = audio_text
        self.audio_analysis = json.loads(audio_analysis)


class ErrorBean(object):
    def __init__(self, error="Error"):
        self.status = 0
        self.error = error

