from django.db import models
from datetime import date


class Projects(models.Model):
    auth_user = models.CharField(max_length=128)
    api_key = models.CharField(max_length=256)
    asset_id = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    server_url = models.CharField(max_length=256)
    source_language = models.CharField(max_length=48)
    transcription_language = models.CharField(max_length=48)
    transcription_method = models.CharField(max_length=128)
    transcription_table = models.CharField(max_length=256)
    upload_date = models.DateField(default=date.today)
