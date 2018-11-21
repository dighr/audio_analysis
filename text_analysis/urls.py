from django.urls import path
from . import views

urlpatterns = [
    path('text_analysis/', views.text_analysis, name='text_analysis'),
]
