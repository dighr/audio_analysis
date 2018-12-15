from django.urls import path
from . import views

urlpatterns = [
    path('text/analyze', views.TextAnalysisView().as_view(), name='text-analysis'),
    path('text/translate', views.TranslationView.as_view(), name='text-translation'),
    path('audio/analyze', views.AudioAnalysisView.as_view(), name='audio-analysis'),
    path('audio/transcribe', views.TranscriptionView.as_view(), name='audio-transcription'),
]
