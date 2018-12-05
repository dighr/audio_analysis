
# This class acts a bean. Required to convert a python object into json
import json


class AnalyzedTextBean(object):
    def __init__(self, analysis="{}"):
        self.status = 1
        self.analysis = json.loads(analysis)


class AnalyzedAudioBean(object):
    def __init__(self, audio_text="", audio_analysis="{}"):
        self.status = 1
        self.audio_text = audio_text
        self.audio_analysis = json.loads(audio_analysis)


class ErrorBean(object):
    def __init__(self, error="Error"):
        self.status = 0
        self.error = error

