from django.db import models
from datetime import date

class Files(models.Model):
    audio_file_name = models.CharField(max_length=256)
    audio_file_path = models.CharField(max_length=256)
    transcribed_file_name = models.CharField(max_length=256)
    transcribed_file_path = models.CharField(max_length=256)
    upload_date = models.DateField(default=date.today)
