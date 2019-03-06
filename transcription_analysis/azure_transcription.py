import json
import time

import requests


def stream_audio_file(speech_file):
    # Chunk audio file
    with open(speech_file, 'rb') as f:
        while 1:
            data = f.read()
            if not data:
                break
            yield data


class AzurTranscription:
    ctime = None

    def __init__(self, api_key, region='eastus',
                 mode='interactive', lang='en-US', format='simple'):
        self.api_key = api_key
        self.token = None
        self.region = region
        self.mode = mode
        self.lang = lang
        self.format = format

    def load_token(self):
        if AzurTranscription.ctime is None:
            AzurTranscription.ctime = time.time()
        # Return an Authorization Token by making a HTTP POST request to Cognitive Services with a valid API key.
        url = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'
        headers = {
            'Ocp-Apim-Subscription-Key': self.api_key
        }
        r = requests.post(url, headers=headers)
        token = r.content
        self.token = token

    def transcribe(self, audio_file):
        now = time.time()
        if self.token is None or now - AzurTranscription.ctime >= 540:
            self.load_token()
            AzurTranscription.ctime = now

        # Request that the Bing Speech API convert the audio to text
        url = 'https://{0}.stt.speech.microsoft.com/speech/recognition/{1}/cognitiveservices/v1?language={2}&format={3}'.format(
            self.region, self.mode, self.lang, self.format)
        headers = {
            'Accept': 'application/json',
            'Ocp-Apim-Subscription-Key': self.api_key,
            'Transfer-Encoding': 'chunked',
            'Content-type': 'audio/wav; codec=audio/pcm; samplerate=16000',
            'Authorization': 'Bearer {0}'.format(self.token)
        }
        r = requests.post(url, headers=headers, data=stream_audio_file(audio_file))
        results = json.loads(r.content)
        return results['DisplayText'] if results["RecognitionStatus"] == "Success" else ""
