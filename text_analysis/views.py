# Create your views here.
from django.http import HttpResponse
import text_analysis.text_analysis as analysis
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from text_analysis.beans import AnalyzedAudioBean, ErrorBean
from .serializers import FileSerializer
import json


# Supports only post request.
# An audio file of the "war" format needs to be provided within the request
# the file has to be less than one minute long for now
class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)
        # Check for validity
        if file_serializer.is_valid():
            # save the file
            file_serializer.save()
            # get file name
            try:
                file_name = file_serializer.data['file']
                # Get both the transcription and the analysis
                text = analysis.transcribe_short_audio(file_name)
                resp = analysis.get_text_sentiment_values(text)
                audio_bean = AnalyzedAudioBean(audio_text=text, audio_analysis=resp)
                resp = json.dumps(audio_bean.__dict__)
                return HttpResponse(resp, content_type="text/json")

            except Exception as e:
                return HttpResponse(analysis.get_error_message(str(e)), content_type="text/json")
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get the text analysis in JSON
# to get valid response, text and method has to be provided in the parameter
class TextAnalysisView(APIView):
    def get(self, request):
        text = request.GET.get('text')
        method = request.GET.get('method')

        if (text is not None) and (method is not None):
            if method == "google":
                try:
                    value = analysis.get_text_sentiment_values(text)
                except Exception as e:
                    analysis.get_error_message(str(e))
            else:
                value = analysis.get_error_message("The method specified is not supported")
        else:
            value = analysis.get_error_message("'text' and 'method' were not passed in the argument")

        return HttpResponse(value, content_type="text/json")


# def text_analysis(request):
#     if request.method == 'GET':
#         text = request.GET.get('text')
#         method = request.GET.get('method')
#
#         if (text is not None) and (method is not None):
#             if method == "google":
#                 value = analysis.get_text_sentiment_values(text)
#             else:
#                 value = analysis.get_error_message("The method specified is not supported")
#         else:
#             value = analysis.get_error_message("'text' and 'method' were not passed in the argument")
#
#         return HttpResponse(value, content_type="text/json")

