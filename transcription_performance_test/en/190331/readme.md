## Content
This folder contains the transcription results of english audios obtained by using the following APIS
 - Azure
 - Google
 - Watson
 - Deepspeech

## Dataset 
The dataset used within this expirement were taken from 
"https://voice.mozilla.org/en/datasets" open source dataset (new version)
The list of files used can be obtained by openning the file

## Transcription Procedure
Explained in the readme.md file of the parent directory of this folder

## Scores
The results reported within each file use two different methods
   - Word Error Rate (WER): *The value shown with the csv files are 1 - WER" which identify similarity rather than error
      * The following python package was used to calculate WER: 
      * For more info about(WER): https://en.wikipedia.org/wiki/Word_error_rate 
   - Similarity Score: 
      * The scores were calculated using suggestion from the following median article
                https://towardsdatascience.com/overview-of-text-similarity-metrics-3397c4601f50
      * The implemetation "get_similarity_scores" is under the test.py file
      * In all the expirements made, this method reported less scores than (1 - WER)
       
