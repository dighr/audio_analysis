from django.db import models


class AudioFile(models.Model):
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)


class TextAnalysis(models.Model):
    text = models.TextField()
    method = models.CharField(max_length=30)
    sentiment = models.FloatField()
    magnitude = models.FloatField()

