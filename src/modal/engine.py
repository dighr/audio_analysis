# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


class Engine:
    __instance = None

    def __init__(self):
        """ Virtually private constructor. """
        if Engine.__instance is not None:
            raise Exception("This class is a singleton! Call the instance methods")
        else:
            Engine.__instance = self

    def get_text_sentiment_values(self, text):
        # Instantiates a client
        client = language.LanguageServiceClient()

        # The text to analyze
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)

        # Detects the sentiment of the text
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        return sentiment.score, sentiment.magnitude

    @staticmethod
    def get_instance():
        if Engine.__instance is None:
            Engine.__instance = Engine()
        return Engine.__instance



