from django.db import models
import os

audio_directory_path = os.path.join('.', 'audio_files')


class AudioFile(models.Model):
    file = models.FileField(upload_to=audio_directory_path)
    # remark = models.CharField(max_length=20)
    # timestamp = models.DateTimeField(auto_now_add=True)


class TextAnalysis(models.Model):
    text = models.TextField()
    method = models.CharField(max_length=30)
    sentiment = models.FloatField()
    magnitude = models.FloatField()

