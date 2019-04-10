## Content
This folder contains the transcription results of an arabic dataset obtained using the following API
    - Azure
    - google

## Dataset 
This dataset is obtained from the University of oxford text archive
"Arabic Speech corpus" by Nawar Halabi
http://ota.ox.ac.uk/desc/2561

## Transcription Procedure
Explained in the readme.md file of the parent directory of this folder

## Postprocessing of Sentences before Calculating their scores
Every actual and generated results were preprocessed before calculating their scores (implementation is under
    the method "pre_process_arabic_string" in the "test.py")
   - Each arabic sentence is converted into english characters using the buckwalter transliteration 
   - From the converted string, symbols that do not change the meaning of the sentence were removed from the file
   - Other suggested pre-processing were performed like removing extras spaces (Can be looked at from the implementation)
   - WER and Similarity scores were used to calculate similarity of sentences
