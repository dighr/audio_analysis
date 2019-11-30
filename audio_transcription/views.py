
# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView
import audio_transcription.engine as engine

# Supports only post requests.
# An audio file of "wav, MP3, or " format needs to be provided within the request
class AudioAnalysisView(APIView):
    def post(self, request):
        file = request.FILES.get("file")
        language_code = request.POST.get("language_code")
        response = engine.handle_audio_analysis_request(file, language_code)
        return HttpResponse(response, content_type="text/json")


# get the text analysis in JSON
# to get valid response, text and method has to be provided in the parameter
class TextAnalysisView(APIView):
    def post(self, request):
        text = request.POST.get('text')
        method = request.POST.get('method')
        source_language = request.POST.get('language_code')
        response = engine.handle_text_analysis_request(text, source_language, method)
        return HttpResponse(response, content_type="text/json")


# Transcribe an audio file.
# Prerequesite, the language-code should match the audio file
class TranscriptionView(APIView):
    def post(self, request):
        file = request.FILES.get("file")
        language_code = request.POST.get("language_code")
        response = engine.handle_audio_transcription_request(file, language_code)
        return HttpResponse(response, content_type="text/json")


# Handle Translation API call
class TranslationView(APIView):
    def post(self, request):
        text = request.POST.get("text")
        source_language = request.POST.get("language_code")
        response = engine.handle_translation_request(text, source_language)
        return HttpResponse(response, content_type="text/json")

# Handle retrieve API call
class RetrieveView(APIView):
    def post(self, request):
        kpi_assetid = request.POST.get("assetid")
        api_token = request.POST.get("token")
        response = engine.handle_retrieve_request(kpi_assetid, api_token)
        return HttpResponse(response, content_type="text/json")
