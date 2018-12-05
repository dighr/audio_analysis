from django.urls import path
from . import views

urlpatterns = [
    path('text/analyze', views.TextAnalysisView().as_view(), name='text-analysis'),
    path('audio/analyze', views.FileView.as_view(), name='file-upload')
]
