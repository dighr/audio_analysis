import os
from watson_developer_cloud import SpeechToTextV1


class WatsonTranscription:
    def __init__(self, api_key=os.getenv("WATSON_KEY"), url="https://stream.watsonplatform.net/speech-to-text/api"):
        print(api_key)
        self.speech_to_text = SpeechToTextV1(
            iam_apikey=api_key,
            url=url
        )

    def transcribe(self, audio_path):
        with open(audio_path, 'rb') as audio_file:
            response = self.speech_to_text.recognize(
                audio=audio_file,
                content_type='audio/wav',
            ).get_result()
        # print(response)
        return response["results"][0]["alternatives"][0]["transcript"] \
            if len(response["results"]) > 0 and response["result_index"] == 0 else ""
