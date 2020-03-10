from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import audio_transcription.engine as engine
from audio_transcription.forms import ProjectForm
from audio_transcription.models import Projects
from audio_transcription.models import Files
from django.views.generic.list import ListView

# Lists the project - also serves as the homepage
class ProjectListView(ListView):
    model = Projects
    context_object_name = 'project_list'
    template_name = 'projects/project_list.html'
    
    def get(self, request):
        project_list = Projects.objects.all()
        transcribed_file_count = Files.objects.count()
        return render(request, self.template_name, {'project_list': project_list, 'count': transcribed_file_count})

    
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
    def get(self, request):
        #kpi_assetid = request.POST.get("assetid")
        #api_token = request.POST.get("token")
        kpi_assetid = 'aw3aWxHPvVJ48Kv7uhefj5'
        api_token = '52c7a8b6b1f0de7848a55e6d5c47aac3929af767'
        engine.handle_retrieve_request(kpi_assetid, api_token)
        return HttpResponseRedirect('/')

        
# Exports transcribed audio files in csv format
class ExpoetCSVView(APIView):
    def get(self, requesrt):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment;filename=transcribed_audio.csv"

        engine.handle_export_csv_file_request(response) 
        return response

    
# Handle add_project API call
class CreateProjectView(APIView):
    submitted = False
    form_class = ProjectForm
    template_name = 'projects/add_project.html'

    def get(self, request):
        form = self.form_class()
        if 'submitted' in request.GET:
            submitted = True
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

            kpi_assetid = form['asset_id'].value()
            api_token = form['api_key'].value()
            source_language = form.cleaned_data['source_language']
            project_name = form['title'].value()
            engine.handle_retrieve_request(kpi_assetid, api_token, source_language, project_name)

            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form, 'submitted': submitted})
