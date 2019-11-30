from django.db import models
from datetime import date

class Transcription_text(models.Model):
    audio_file_name = models.CharField(max_length=256)
    transcribed_file_name = models.CharField(max_length=256)
    upload_date = models.DateField(default=date.today)
