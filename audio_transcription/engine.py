import binascii
import json
import os
import tempfile
import wave
import requests
import sys
import urllib.request
from urllib.error import HTTPError

from google.protobuf.json_format import MessageToJson
from pydub import AudioSegment
from audio_transcription.beans import ErrorBean, ResponseBean
from audio_transcription.google_transcription import translate_text_from
from audio_transcription.google_transcription import get_text_sentiment_values
from audio_transcription.models import Transcription_text

audio_directory_path = os.path.join('.', 'converted_audio_files')
# directory name where the audio files be downloaded
dirname = os.path.join('.', 'audio_files')

# given a text and a method, retreive the sentiment of that text using method modal
def handle_text_analysis_request(text, language_code,  method):
    global value
    if (text is not None) and (method is not None) and (language_code is not None):
        if method == "google":
            try:
                text_to_analyze = text

                if str(language_code).lower() != 'en':
                    translated_text_obj = translate_text_from(text, language_code)
                    text_to_analyze = translated_text_obj['translation']

                text_analysis = MessageToJson(get_text_sentiment_values(text_to_analyze))

                response = {
                    'text': text,
                    'language_code': language_code,
                    'translation': text_to_analyze,
                    'text_analysis': json.loads(text_analysis)
                }

                text_bean = ResponseBean(response)
                value = json.dumps(text_bean.__dict__)
            except Exception as e:
                value = get_error_message(str(e))
        else:
            value = get_error_message("The method specified is not supported")
    else:
        value = get_error_message("'text' or 'method' or 'source_language' were not passed in the argument")

    return value


def handle_translation_request(text, language_code):
    global value
    if (language_code is not None) and (text is not None):

        try:
            resp = translate_text_from(text, str(language_code).split("-")[0])
            translation_bean = ResponseBean(resp)
            value = json.dumps(translation_bean.__dict__)
        except Exception as e:
            value = get_error_message(str(e))
    else:
        value = get_error_message("'text' and 'language_code' were not passed in the argument")

    return value


# given a file on instance of UploadedFile, transcribe and analyze the audio
def handle_audio_analysis_request(file_obj, language_code="en-US"):
    try:
        # Transcribe
        text = transcribe_any_audio(file_obj, language_code,  type="google")

        # translate the text if language_code is not english
        iso = str(language_code).split("-")[0]
        translation = text
        if iso.lower() != 'en':
            translation = translate_text_from(text, iso.lower())['translation']

        # Do a sentiment analysis on the transcribed text
        text_analysis = MessageToJson(get_text_sentiment_values(translation))

        # return the answers in a JSON format
        response = {
            'audio_text': text,
            'translation': translation,
            'audio_analysis':  json.loads(text_analysis)
        }

        # Create an success bean object
        audio_bean = ResponseBean(response)

        # return the response as json
        return json.dumps(audio_bean.__dict__)

    except Exception as e:
        return get_error_message(str(e))


# given a file on instance of UploadedFile, transcribe the audio
def handle_audio_transcription_request(file_obj, language_code="en-US"):
    try:
        # Get the transcribed text
        text = transcribe_any_audio(file_obj, language_code, type="google")

        # translate the text if language_code is not english
        iso = str(language_code).split("-")[0]
        translation = text
        if iso.lower() != 'en':
            translation = translate_text_from(text, iso.lower())['translation']

        # return the answer in a JSON format
        response = {
            'file_name': file_obj.name,
            'audio_text': text,
            'translation': translation,
        }

        audio_text_bean = ResponseBean(response)
        return json.dumps(audio_text_bean.__dict__)
    except Exception as e:
        return get_error_message(str(e))


def transcribe_any_audio(file_obj, language_code, type):
    # convert the given file into a supported file
    file_name = convert_audio_to_wav(file_obj)
    if file_name is None:
        raise Exception("File was not provided or the provided file is not in the following"
                        " format (WAV, MP3, OGG)")

    if type == "google":
        from audio_transcription.google_transcription import GoogleTranscription
        gt = GoogleTranscription(language_code)
        gt.transcribe(file_name)

    # Remove file_name
    os.remove(file_name)


def get_error_message(error):
    error_obj = ErrorBean(error)
    return json.dumps(error_obj.__dict__)


# Convert the uploaded audio file to wav if they are not and store them under the audio files folder
def convert_audio_to_wav(file, audio_directory=audio_directory_path, add_id=True):
    if file is None:
        return

    if type(file) == str:
        file_name = str(file).split("/")[-1]
        tempfn = file
    else:
        file_name = file.name
        tempf, tempfn = tempfile.mkstemp()
        for chunk in file.chunks():
                os.write(tempf, chunk)
        os.close(tempf)

    # audio_directory is required to store the converted files,
    # create it if it does not exist
    if not os.path.exists(audio_directory):
        os.makedirs(audio_directory)

    id = ""
    if add_id:
        id = str(binascii.hexlify(os.urandom(32)).decode())
    file_path = os.path.join(audio_directory, os.path.splitext(file_name)[0] + id + ".wav")
    # Encoding Audio file into Wav
    if file_name.endswith('.mp3'):
        sound = AudioSegment.from_mp3(tempfn)
        out = sound.export(file_path, format="wav")
        out.close()
    elif file_name.endswith('.ogg'):
        sound = AudioSegment.from_ogg(tempfn)
        out = sound.export(file_path, format="wav")
        out.close()
    elif file_name.endswith('.wav'):
        sound = AudioSegment.from_wav(tempfn)
        out = sound.export(file_path, format="wav")
        out.close()
    elif file_name.endswith(".flac"):
        sound = AudioSegment.from_file(tempfn, "flac")
        # os.system("sox " + tempfn + " " + file_path)
        out = sound.export(file_path, format="wav")
        out.close()
    elif file_name.endswith(".m4a"):
        sound = AudioSegment.from_file(tempfn, "m4a")
        out = sound.export(file_path, format="wav")
        out.close()

    return file_path

# downloads audio file into a directory
def download_file(url, req_header):
    filename = url.split('/')[-1]
    file_path = os.path.join(dirname, filename)

    # checks and creates the directory if not exists
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    # checkes if the file has already been downloaded
    # if found skips downloading
    if os.path.isfile(file_path):
        print('Skipping... File already exists.')
        return 'found'

    try:
        response = requests.get(url, stream = True, headers=req_header)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return 'error'
    except Exception as err:
        print(f'Other error occurred: {err}')
        return 'error'
    else:
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size = 1024):
                if chunk:
                    f.write(chunk)
                    f.flush()

    return file_path

def handle_retrieve_request(assetid, token):
    kpiAssetID = assetid
    apiToken = 'Token ' + token

    url = 'https://kf.kobotoolbox.org/api/v2/assets/' + kpiAssetID + '/data.json'
    headers = { 'Authorization': apiToken }

    try:
        response = requests.get(url, headers=headers)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        # converts response as JSON object
        response = response.json()
        # iterates the response body to retrieve all the download urls and
        # downloads the audio files.
        for (key, value) in response.items():
            if key == 'results':
                for item in value:
                    for (key, value) in item.items():
                        if key == '_attachments':
                            for item in value:
                                for (key, value) in item.items():
                                    if key == 'download_url' and (value.endswith('.mp3') or value.endswith('.wav') or value.endswith('.m4a') or value.endswith('.ogg') or value.endswith('.flac')):
                                        audio_url = value
                                        file = download_file(audio_url, headers)
                                        if file == 'found':
                                            pass
                                        elif file == 'error':
                                            print("Status: Failed to download, try again.")
                                        elif file is not None:
                                            filename = file.split('/')[-1]
                                            print(filename + " ===> Status: Download completed.")

                                            # store audio file info into the database
                                            name = Transcription_text(audio_file_name=filename)

                                            name.save()

                                            print("Starting to transcribe ...")
                                            handle_audio_transcription_request(file, 'en-US')
                                            print('Transcription Completed.\n')
                                        else:
                                            print("Status: Failed to download, try again.")

    return 'Retrival Completed.'
