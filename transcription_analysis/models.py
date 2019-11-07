from django.db import models

class FileManager(models.Manager):
    def add_audio_file(self, path):
        self.create(audio_file_path=path)

    def add_transcribed_file(self, path):
        self.create(transcribed_file_path=path)

class Files(models.Model):
    audio_file_path = models.CharField(max_length=128)
    transcribed_file_path = models.CharField(max_length=128)
    upload_date = models.DateField()

    objects = FileManager()
