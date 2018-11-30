from django.urls import path
from . import views

urlpatterns = [
    path('transcription_analysis/', views.TextAnalysisView().as_view(), name='text-analysis'),
    path('upload/', views.FileView.as_view(), name='file-upload')
]
