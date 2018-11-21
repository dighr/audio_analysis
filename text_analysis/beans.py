

# This class acts a bean. Required to convert a python object into json
class AnalyzedTextBean(object):
    def __init__(self, text="", score=-2, magnitude = -2):
        self.status = 1
        self.text = text
        self.score = score
        self.magnitude = magnitude


class ErrorBean(object):
    def __init__(self, error="Error"):
        self.status = 0
        self.error = error

