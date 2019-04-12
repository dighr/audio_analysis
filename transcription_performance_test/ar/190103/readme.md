Steps taken to obtain the arabic sentences
- Available English sentences were taken from Mozilla’s `voice-web` repository based on confirmed sentences validated by the community. 
      * (https://github.com/mozilla/voice-web/blob/master/server/data/en/sentence-collector.txt)
      * (https://github.com/mozilla/voice-web/blob/master/server/data/en/harvsents.txt)
- Using Google’s translation API, each one of these sentences were translated to Arabic
- Each pair of English sentences and the translated Arabic were then added as separate columns in a CSV file, which was uploaded to Google Spreadsheets
- Native Arabic speakers went (are going) through each machine-translated phrase and flag the ones that are correct (1) or have some error (0). If a sentence seems to be correct but makes no sense in Arabic (maybe because it was an English idiom or a phrase that only made sense in the original English), enter 0.
- Incorrect sentences should be corrected. Once corrected, the status can be changed to 1. Otherwise we will simply not upload the sentence.
- Correct phrases are then added to the Sentence Collector with the upload date specified. 