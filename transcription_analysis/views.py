# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
import transcription_analysis.engine as engine


# Supports only post requests.
# An audio file of "wav" format needs to be provided within the request
# the file has to be less than one minute long for now
class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        response = engine.handle_audio_analysis_request(request.data)
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


# get the text analysis in JSON
# to get valid response, text and method has to be provided in the parameter
class TextAnalysisView(APIView):
    def get(self, request):
        text = request.GET.get('text')
        method = request.GET.get('method')
        response = engine.handle_text_analysis_request(text, method)
        return HttpResponse(response, content_type="text/json")

