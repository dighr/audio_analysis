from rest_framework import serializers
from .models import AudioFile
from .models import TextAnalysis


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFile
        fields = ['file']


class TextAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextAnalysis
        fields = ('text', 'sentiment', 'magnitude')

