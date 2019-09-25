#!/usr/bin/python

import requests
import os
import sys
import urllib.request

dirname = os.path.join('.', 'tmp')

def download_file(url):
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

    r = requests.get(url, stream = True)
    with open(file_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size = 1024): 
            if chunk:
                f.write(chunk)
                f.flush()
    return filename

if len(sys.argv) != 3:
    print('Please provide arguments. Usage: retrieve_kobo_audio.py <kpiAssetID> <apiToken>')
    sys.exit(1)

kpiAssetID = str(sys.argv[1])
apiToken = 'Token ' + str(sys.argv[2])

url = "https://kf.kobotoolbox.org/assets/" + kpiAssetID + "/submissions.json"
headers = { 'Authorization': apiToken }
response = requests.get(url,headers=headers).json()

# iterates the response body to retrieve all the download urls and
# downloads the audio files.
for entity in response:
    audio_url = str(entity['_attachments'][0]['download_url'])
    filename = download_file(audio_url)
    if filename == 'found':
        pass
    elif filename is not None:
        print(filename + " ===> Status: Download completed.")
    else:
        print("Status: Failed to download, try again.")
