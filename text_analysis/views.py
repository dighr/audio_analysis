# Create your views here.
from django.http import HttpResponse
import text_analysis.text_analysis as analysis
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from .serializers import TextAnalysisSerializer


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)
        print(request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TextAnalysisView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        text = request.GET.get('text')
        method = request.GET.get('method')

        if (text is not None) and (method is not None):
            if method == "google":
                value = analysis.get_text_sentiment_values(text)
                data = {"text":  text,
                        "method": method,
                        "sentiment": value[0],
                        "magnitude": value[1],
                        }

                file_serializer = TextAnalysisSerializer(data=data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return Response(file_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def text_analysis(request):
    if request.method == 'GET':
        text = request.GET.get('text')
        method = request.GET.get('method')

        if (text is not None) and (method is not None):
            if method == "google":
                value = analysis.get_text_sentiment_values(text)
            else:
                value = analysis.get_error_message("The method specified is not supported")
        else:
            value = analysis.get_error_message("'text' and 'method' were not passed in the argument")

        return HttpResponse(value, content_type="text/json")

