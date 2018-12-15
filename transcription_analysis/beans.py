
# This class acts a bean. Required to convert a python object into json


class ResponseBean(object):
    def __init__(self, analysis={}):
        self.status = 1
        self.response = analysis


class ErrorBean(object):
    def __init__(self, error="Error"):
        self.status = 0
        self.error = error

