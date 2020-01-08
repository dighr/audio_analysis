from django import forms
from audio_transcription.models import Projects

TRANSCRIPTION_METHOD_CHOICES = (
    ('gcp', 'Google Cloud Platform'),
)

SERVER_URL_CHOICES = (
    ('kobo', 'kfkobotoolbox.org'),
)

TRANSCRIPTION_LANGUAGE_CHOICES = (
    ('en-us', 'English (US)'),
    ('en-uk', 'English (UK)'),
    ('fr-ca', 'French (Canadian)'),
)

class ProjectForm(forms.ModelForm):

    server_url = forms.ChoiceField(choices=SERVER_URL_CHOICES, required=True)
    transcription_language = forms.ChoiceField(choices=TRANSCRIPTION_LANGUAGE_CHOICES, required=True)
    transcription_method = forms.ChoiceField(choices=TRANSCRIPTION_METHOD_CHOICES, required=True)

    class Meta:
        model = Projects
        fields = ['server_url', 'api_key', 'asset_id', 'title', 'transcription_language', 'transcription_method']
