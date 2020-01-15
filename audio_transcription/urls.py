from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [

    path('', login_required(views.ProjectListView.as_view()), name='projects'),
    path('projects/', login_required(views.ProjectListView.as_view()), name='projects'),
    path('text/analyze', views.TextAnalysisView().as_view(), name='text-analysis'),
    path('text/translate', views.TranslationView.as_view(), name='text-translation'),
    path('audio/analyze', views.AudioAnalysisView.as_view(), name='audio-analysis'),
    path('audio/transcribe', views.TranscriptionView.as_view(), name='audio-transcription'),
    path('audio/retrieve', login_required(views.RetrieveView.as_view()), name='audio-retrieve'),
    path('add_project/', login_required(views.CreateProjectView.as_view()), name='add-project'),
    path('export_csv/', login_required(views.ExpoetCSVView.as_view()), name='export-csv'),
]
