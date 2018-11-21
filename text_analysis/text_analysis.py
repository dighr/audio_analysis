# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from text_analysis.beans import AnalyzedTextBean
from text_analysis.beans import ErrorBean
import json


def get_text_sentiment_values(text):
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    sentiment_obj = AnalyzedTextBean(text, sentiment.score, sentiment.magnitude)

    return json.dumps(sentiment_obj.__dict__)


def get_error_message(error):
    error_obj = ErrorBean(error)
    return json.dumps(error_obj.__dict__)


