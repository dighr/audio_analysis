from django import forms
from audio_transcription.models import Projects

TRANSCRIPTION_METHOD_CHOICES = (
    ('gcp', 'Google Cloud Platform'),
)

SERVER_URL_CHOICES = (
    ('ktl', 'kf.kobotoolbox.org'),
    ('khr', 'kobo.humanitarianresponse.info')
    ('hcr', 'kobo.unhcr.org')
)

SOURCE_LANGUAGE_CHOICES = (
    ('en', 'English'),
    ('fr', 'French'),
    ('af', 'Afrikaans'),
    ('sq', 'Albanian'),
    ('am', 'Amharic'),
    ('ar', 'Arabic'),
    ('hy', 'Armenian'),
    ('az', 'Azerbaijani'),
    ('eu', 'Basque'),
    ('be', 'Belarusian'),
    ('bn', 'Bengali'),
    ('bs', 'Bosnian'),
    ('bg', 'Bulgarian'),
    ('ca', 'Catalan'),
    ('ceb', 'Cebuano'),
    ('zh', 'Chinese (Simplified)'),
    ('zh-TW', 'Chinese (Traditional)'),
    ('co', 'Corsican'),
    ('hr', 'Croatian'),
    ('cs', 'Czech'),
    ('da', 'Danish'),
    ('nl', 'Dutch'),
    ('eo', 'Esperanto'),
    ('et', 'Estonian'),
    ('fi', 'Finnish'),
    ('fy', 'Frisian'),
    ('gl', 'Galician'),
    ('ka', 'Georgian'),
    ('de', 'German'),
    ('el', 'Greek'),
    ('gu', 'Gujarati'),
    ('ht', 'Haitian Creole'),
    ('ha', 'Hausa'),
    ('haw', 'Hawaiian'),
    ('he', 'Hebrew'),
    ('hi', 'Hindi'),
    ('hmn', 'Hmong'),
    ('hu', 'Hungarian'),
    ('is', 'Icelandic'),
    ('ig', 'Igbo'),
    ('id', 'Indonesian'),
    ('ga', 'Irish'),
    ('it', 'Italian'),
    ('ja', 'Japanese'),
    ('jv', 'Javanese'),
    ('kn', 'Kannada'),
    ('kk', 'Kazakh'),
    ('km', 'Khmer'),
    ('ko', 'Korean'),
    ('ku', 'Kurdish'),
    ('ky', 'Kyrgyz'),
    ('lo', 'Lao'),
    ('la', 'Latin'),
    ('lv', 'Latvian'),
    ('lt', 'Lithuanian'),
    ('lb', 'Luxembourgish'),
    ('mk', 'Macedonian'),
    ('mg', 'Malagasy'),
    ('ms', 'Malay'),
    ('ml', 'Malayalam'),
    ('mt', 'Maltese'),
    ('mi', 'Maori'),
    ('mr', 'Marathi'),
    ('mn', 'Mongolian'),
    ('my', 'Myanmar (Burmese)'),
    ('ne', 'Nepali'),
    ('no', 'Norwegian'),
    ('ny', 'Nyanja (Chichewa)'),
    ('ps', 'Pashto'),
    ('fa', 'Persian'),
    ('pl', 'Polish'),
    ('pt', 'Portuguese (Portugal, Brazil)'),
    ('pa', 'Punjabi'),
    ('ro', 'Romanian'),
    ('ru', 'Russian'),
    ('sm', 'Samoan'),
    ('gd', 'Scots Gaelic'),
    ('sr', 'Serbian'),
    ('st', 'Sesotho'),
    ('sn', 'Shona'),
    ('sd', 'Sindhi'),
    ('si', 'Sinhala (Sinhalese)'),
    ('sk', 'Slovak'),
    ('sl', 'Slovenian'),
    ('so', 'Somali'),
    ('es', 'Spanish'),
    ('su', 'Sundanese'),
    ('sw', 'Swahili'),
    ('sv', 'Swedish'),
    ('tl', 'Tagalog (Filipino)'),
    ('tg', 'Tajik'),
    ('ta', 'Tamil'),
    ('te', 'Telugu'),
    ('th', 'Thai'),
    ('tr', 'Turkish'),
    ('uk', 'Ukrainian'),
    ('ur', 'Urdu'),
    ('uz', 'Uzbek'),
    ('vi', 'Vietnamese'),
    ('cy', 'Welsh'),
    ('xh', 'Xhosa'),
    ('yi', 'Yiddish'),
    ('yo', 'Yoruba'),
    ('zu', 'Zulu'),
)

TRANSCRIPTION_LANGUAGE_CHOICES = (
    ('en', 'English'),
    ('fr', 'French'),
    ('es', 'Spanish'),
)

class ProjectForm(forms.ModelForm):

    server_url = forms.ChoiceField(choices=SERVER_URL_CHOICES, required=True)
    source_language = forms.ChoiceField(choices=SOURCE_LANGUAGE_CHOICES, required=True)
    transcription_language = forms.ChoiceField(choices=TRANSCRIPTION_LANGUAGE_CHOICES, required=True)
    transcription_method = forms.ChoiceField(choices=TRANSCRIPTION_METHOD_CHOICES, required=True)

    class Meta:
        model = Projects
        fields = ['server_url', 'api_key', 'asset_id', 'title', 'source_language', 'transcription_language', 'transcription_method']
