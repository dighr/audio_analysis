# Audio Analysis
This project is divided into two parts:
- an API is created to transcribe, translate, and analyze the sentiment values of audio files using multiple commercial APIs. 
- Determining the accuracy of multiple commercial transcription models by transcribing 4070 audio files against each model 
### Prerequisites
All of the following needs to be downloaded in your device
 * Python 3.6
 * virtualenv
 * pip
   * Make sure that the folder where python is downloaded is in the enviroment variable
 * Google Cloud Platform API key
Optional: 
 * Deepspeech pre-trained model

### Setting up
 * download the github repo  
```
  git clone https://github.com/dighr/audio_analysis.git
  
``` 
* Navigate to the cloned repo
* Create a python virtualenv 
```
virtualenv -p python3 env
```
* Activate the virtual environment
``` 
source env/bin/activate
```
     * In windows the command is 
``` 
source env/Scripts/activate
```
* Download all the dependencies
```
pip install -r requirements.txt
```

* Add the GOOGLE_APPLICATION_CREDENTIALS into the enviroment variables
  * If you don't have an account yet, create an account https://cloud.google.com/
  * Within the google cloud console, create a new project
  * Within the created project, enable the NLP API and the audio-to-text API
  * Create a service
  * Download the credentials of the created service as JSON
  * Add an enviroment variable named GOOGLE_APPLICATION_CREDENTIALS 
    and point the downloaded JSON file into it
       * In linux, just execute the following in the terminal
       ```
         export  GOOGLE_APPLICATION_CREDENTIALS=path-to-the-downloaded-json-file
       ```
       
  * Add an environment variable to store the private API keys of both Watson and Azure
   
    
## Getting Started
Assuming that the previous section is complete, you can start the server by executing the following in  a terminal
 ```
python manage.py runserver
 ```         
 
## Making API calls

### language_code for both 'audio/transcribe' and 'audio/analyze'
The API calls to transcribe audios require a language_code as a parameter to be passed in within the body.
Find the correct language code from the following URL
https://cloud.google.com/speech-to-text/docs/languages

### language_code for both 'text/analyze' and text/translate'
Both 'text/analyze' and 'text/translate' API also requires 'language_code' as a parameter when making an API call. 
Use the correct ISO-639-1 Code value for 'language_code from the link below
https://cloud.google.com/translate/docs/languages

### API CALLS
To analyze a text, make a post request  to the following URL
PASS in both text=text_to_be_analyzed, method=google, and language_code  into the body
 ```
 http://localhost:PORT/text/analyze
 ```
 
To translate a text, make a post request to the following URL
Provide  both 'text' (text_to_be_translated) and 'source_language' (Explained above) as an input to make the translation
 ```
 http://localhost:PORT/text/translate
 ```

 To transcribe an audio file, make a post request to the following URL
 ```
 http://localhost:PORT/audio/transcribe
 ```
 Attach the audio file within the body of the request in the following format
'file=audio_file_path'
pass in the 'language_code' parameter into the body


 To analyze an audio file, make a post request to the following URL
 ```
 http://localhost:PORT/audio/analyze
 ```
 Attach the audio file within the body of the request in the following format
'file=audio_file_path'
pass in the language_code parameter into the body

 
# Sample Output

## Running the tests
 ```
python manage.py test
 ```


## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

* A lot of functionality was enabled thanks to the Pydub library https://github.com/jiaaro/pydub
* For long audio files, a method created by the following git repo 	https://github.com/akras14/speech-to-text.git was used. 
 However, we made the process of audio encoding and the audio file splitting automatic

