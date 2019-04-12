from __future__ import print_function
import glob
import os

import pandas as pd
from jiwer import wer
from sklearn.feature_extraction.text import TfidfVectorizer
from transcription_analysis import engine


def change_name(path, name, ext):
    """
     Rename all files with extension ext within path with the name "name"
    :param path: the path where the files are located
    :param name: The new name added before the incremented index
    :param ext: the extension
    :return:
    """
    results = [os.path.basename(f) for f in glob.glob(os.path.join(path, ext))]
    for index in range(len(results)):
        os.rename(path + results[index], path + (name + index + ext))


def get_similarity_score(str1, str2):
    """
    The common way of comparing similarity is to transform the texts into tf-idf vectors,
    then the cosine similarity between both of the strings.
         See https://towardsdatascience.com/overview-of-text-similarity-metrics-3397c4601f50
    Tf-idf (and similar text transformations) are implemented in the Python packages Gensim and
    scikit-learn. In our fuction, sickit-learn was used.
    """
    documents = [str1, str2]
    tfidf = TfidfVectorizer().fit_transform(documents)
    # no need to normalize, since Vectorizer will return normalized tf-idf
    pairwise_similarity = tfidf * tfidf.T

    # Get the average similarity between the two sentences
    return (pairwise_similarity[1, 0] + pairwise_similarity[0, 1]) / 2


# Transcribe audios and translate file. Store the result into a csv file
def transcribe_audios(file_paths, format="mp3", modal_code="en-US", type="deepspeech"):
    # Get result from the engine transcription
    audio_files = [(file_paths + os.path.basename(f)) for f in glob.glob(os.path.join(file_paths, '*.' + format))]
    audio_files.sort()
    transcribe_audios_from_list(audio_files, format, modal_code, type)


def transcribe_audios_from_list(audio_files, format, modal_code, type):
    # Get result from the engine transcription
    transcription_output = []
    translation_output = []
    files = []
    for index in range(len(audio_files)):

        transcription = engine.transcribe_any_audio(audio_files[index],
                                                        modal_code, type=type)

        files.append(audio_files[index].split(format)[0])
        transcription_output.append(transcription)

        print(index, audio_files[index], transcription, type)

        # Save regularly. After every 10 transcription
        if index % 10 == 0:
            output_dictionary = {"files": files,
                                 "transcription_" + modal_code: transcription_output,
                                 # "translation_" + modal_code: translation_output
                                 }
            df = pd.DataFrame(data=output_dictionary)
            df.to_csv(type + "_transcription_output_" + modal_code + ".csv")

    # last save
    output_dictionary = {"files": files,
                         "transcription_" + modal_code: transcription_output,
                         # "translation_" + modal_code: translation_output
                         }
    df = pd.DataFrame(data=output_dictionary)
    df.to_csv(type + "_transcription_output_" + modal_code + ".csv")

def pre_process_arabic_string(str):

    from lang_trans.arabic import buckwalter
    import re
    # Remove all non alphabitic symbols
    output = buckwalter.trans(re.sub(r'([^\s\w]|_)+', '', str))
    # Remove all symbols
    reg = re.compile('[aui~oFNK]')
    output = reg.sub('', output)

    # remove the space before single letter
    output = output.replace(" w ", " w")
    output = output.replace("w ", "w")

    # replace ta marbootah with ha
    output = output.replace("p", "h")

    # replace alif at the end
    output = output.replace("a ", "")

    # Replace different shapes of alf into a single one
    reg = re.compile('[|><]')
    output = reg.sub('A', output)

    # Convert the string back
    return buckwalter.untrans(output)


# transcribe all the audios using the en-US modal
def add_scores_into_csv(excel_file, actual_col, generated_col, arabic=True):
    # Read the excel file
    excel = pd.read_csv(excel_file, encoding="ISO-8859-1")
    excel_values = excel.values

    for index in range(0, len(excel_values)):
        actual = str(excel.at[index, actual_col]).replace(".", "").replace("?", "").replace("!", "").lower()
        generated = str(excel.at[index, generated_col]).lower()

        score = get_similarity_score(actual, generated)
        word_er = wer(actual, generated)
        word_er = 1 if word_er > 1 else word_er
        excel.at[index, "word_error_rate"] = 1 - word_er
        excel.at[index, "scores"] = score

        print("actual: ", actual)
        print("generated: ", generated)
        print(1 - word_er)

    excel.to_csv(excel_file)


# transcribe all the audios using the en-US modal
def transcribe_arabic(audio_file_path, transcription_file_path,
                      audio_format='wav', trans_format="lab", modal_code="ar-EG",
                      type="azure"):
    from lang_trans.arabic import buckwalter

    # Read the excel file
    audio_files = [os.path.basename(f)
                   for f in glob.glob(os.path.join(audio_file_path, '*.' + audio_format))]
    transcription_files = [os.path.basename(f)
                           for f in glob.glob(os.path.join(transcription_file_path, '*.' + trans_format))]

    audio_files.sort()
    transcription_files.sort()

    audios = []
    actual_trans = []
    generated_trans = []
    scores = []

    for index in range(0, len(audio_files)):
        audio_file = audio_files[index]
        audios.append(audio_file)

        transcription = engine.transcribe_any_audio(audio_file_path + audio_file,
                                                    modal_code, type=type)
        transcription = pre_process_arabic_string(transcription)
        generated_trans.append(transcription)

        with open(transcription_file_path + transcription_files[index], 'r') as file:
            actual = file.read().replace('\n', '')

        actual = buckwalter.untrans(actual)
        actual = pre_process_arabic_string(actual)
        actual_trans.append(actual)

        print(index, actual, transcription)

        word_er = wer(buckwalter.trans(actual), buckwalter.trans(transcription))
        word_er = 1 if word_er > 1 else word_er
        scores.append(1 - word_er)

        # Save Regularly
        if index % 10 == 0:
            output_dictionary = {"audio files": audios,
                                 "actual": actual_trans,
                                 "generated": generated_trans,
                                 "scores": scores
                                 }

            df = pd.DataFrame(data=output_dictionary)
            df.to_csv("transcription_output.csv")

        print(audio_file, transcription_files[index])
        print("actual: ", actual)
        print("generated: ", transcription)
        print("score", word_er)

    output_dictionary = {"audio files": audios,
                         "actual": actual_trans,
                         "generated": generated_trans,
                         "scores": scores
                         }

    df = pd.DataFrame(data=output_dictionary)
    df.to_csv("transcription_output.csv")


def translate_texts_from_csv(excel_file, actual_english_col):
    # Read the excel file
    excel = pd.read_csv(excel_file)
    excel_values = excel.values

    translation_output = []
    english_sentences = []
    for index in range(0, len(excel_values)):
        actual = excel.at[index, actual_english_col].replace(".", "")
        english_sentences.append(actual)

        translation = engine.translate_text_from(actual,
                                                 source_language='en', target_language='ar')

        translation_output.append(translation['translation'])
        print(index, actual, translation['translation'])
        if index % 10:
            output_dictionary = {
                "sentences": english_sentences,
                "translation": translation_output

            }
            df = pd.DataFrame(data=output_dictionary)
            df.to_csv("translated_output_ar" + ".csv")

    output_dictionary = {
        "sentences": english_sentences,
        "translation": translation_output

    }
    df = pd.DataFrame(data=output_dictionary)
    df.to_csv("translated_output_ar" + ".csv")


def only_include_non_english(excel_file, col):
    # Read the excel file
    excel = pd.read_csv(excel_file)
    excel_values = excel.values

    translation_output = []
    english_sentences = []
    for index in range(0, len(excel_values)):
        actual = excel.at[index, "sentences"].replace(".", "")
        trans = excel.at[index, col]
        if not has_english_chars(trans):
            english_sentences.append(actual)
            translation_output.append(trans)
            print(index, trans, actual)

    output_dictionary = {
        "sentences": english_sentences,
        "translation": translation_output
    }

    df = pd.DataFrame(data=output_dictionary)
    df.to_csv("translated_output_ar5" + ".csv")


def has_english_chars(test_str):
    import re
    pattern = r'[a-zA-Z]'
    if re.search(pattern, test_str):
        return True

    return False


def match_string_to_audio():
    new = pd.read_csv("test.csv", delimiter="\t")
    print(new.shape)
    old = pd.read_csv("cv-other-test.csv", delimiter=",")
    # print(new)
    print(old.shape)
    new_len = len(new.values)
    old_len = len(old.values)
    sentences = []
    paths = []
    for o in range(old_len):
        # get the actual old text
        actual = (str(old.at[o, "text"]).replace(".", "")).lower()
        # print (actual)
        for n in range(new_len):
            # current =  (str(new.at[n, "sentence"]).replace(".", "")).lower()
            current = (str(new.at[n, "sentence"]).replace(".", "")).lower()
            # print(actual, current)
            if current == actual:
                sentences.append(actual)
                # print("In")
                path = str(new.at[o, "path"]) + ".mp3"
                paths.append(path)
                # print(actual, path)

    output_dictionary = {
        "paths": paths,
        "sentences": sentences
    }

    df = pd.DataFrame(data=output_dictionary)
    df.to_csv("actual_file" + ".csv")


# Transcribe audios and translate file. Store the result into a csv file
def transcribe_audios2(audio_path, csv_file, start=0, format="mp3", modal_code="en-US", type="deepspeech"):
    # Get result from the engine transcription
    excel_csv = pd.read_csv(csv_file, delimiter=",")

    print(excel_csv.shape)
    csv_len = len(excel_csv.values)
    paths = []
    for index in range(start, csv_len):
        # print(audio_path + str(excel_csv.at[index, "paths"]))
        paths.append(audio_path + str(excel_csv.at[index, "paths"]))

    transcribe_audios_from_list(paths, format, modal_code, type)


def aws_bucket_upload(audio_path, csv_file):
    import boto3
    bucketName = "audios2019"
    excel_csv = pd.read_csv(csv_file, delimiter=",")

    print(excel_csv.shape)
    csv_len = len(excel_csv.values)
    paths = []
    for index in range(0, csv_len):
        # print(audio_path + str(excel_csv.at[index, "paths"]))
        paths.append(audio_path + str(excel_csv.at[index, "paths"]))
        Key = audio_path + str(excel_csv.at[index, "paths"])
        outPutname = str(excel_csv.at[index, "paths"])
        print(index, Key)
        s3 = boto3.client('s3')
        s3.upload_file(Key, bucketName, outPutname)


def transcribe_aws():
    import time
    import boto3
    transcribe = boto3.client('transcribe')
    job_name = "test3"
    job_uri = "https://s3.amazonaws.com/audios2019/0094552cf0d521e64b0b727c263c605a399ef31b181b97e491dfa76fd7f88e17cd2bb9dac483ffe41ca47e48975c5bf22d9b0294474724259c8f286b6ef8aa03.mp3"
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='mp3',
        LanguageCode='en-US'
    )
    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        print("Not ready yet...")
        time.sleep(5)

    client = boto3.client('transcribe')
    client.delete_transcription_job(TranscriptionJobName=job_name)
    print(status)


def extract_data_set(language_code):
    """
    Extract ids based on the language_code from https://tatoeba.org/eng/downloads
    :param language_code:
    :return:
    """
    csv = pd.read_csv("sentences.csv", delimiter="\t", header=None)
    rows = csv.shape[0]
    print(rows)
    ids = []
    langs = []
    sentences = []

    for row in range(0, rows):
        lang = csv.at[row, 1]
        if lang == language_code:
            ids.append(csv.at[row, 0])
            langs.append(csv.at[row, 1])
            sentences.append(csv.at[row, 2])

    dictionary = {
        "ID": ids,
        "langs": langs,
        "sentences": sentences
    }

    print(len(sentences))
    # save
    df = pd.DataFrame(data=dictionary)
    df.to_csv("arabic_sentences.csv")


def audios():
    csv = pd.read_csv("sentences_with_audio.csv", delimiter="\t", header=None)
    # print(csv)
    arabic_sentences = pd.read_csv("arabic_sentences.csv", delimiter=",")
    rows = arabic_sentences.shape[0]
    csv_len = csv.shape[0]
    print(arabic_sentences.shape, csv.shape)
    # print(csv.at[0, 1])
    pos = 0
    ids = []
    sentences = []
    for row in range(0, rows):

        if pos >= csv_len:
            print("IN")
            break

        arabic_id = arabic_sentences.at[row, "ID"]
        # print(arabic_id)
        audio_id = csv.at[pos, 0]

        while audio_id < arabic_id:
            audio_id = csv.at[pos, 0]
            pos = pos + 1

        print(audio_id, arabic_id)

        if audio_id == arabic_id:
            # Save
            print(arabic_sentences.at[pos, "sentences"])
            ids.append(arabic_id)
            sentences.append(arabic_sentences.at[pos, "sentences"])
            pos = pos + 1

    dictionary = {
        "ids": ids,
        "sentences": sentences
    }

    df = pd.DataFrame(data=dictionary)
    df.to_csv("arabic_sentencs_with_audio.csv")


def audios2():
    csv = pd.read_csv("sentences_with_audio.csv", delimiter="\t", header=None)
    # print(csv)
    arabic_sentences = pd.read_csv("arabic_sentences.csv", delimiter=",")
    rows = arabic_sentences.shape[0]
    csv_len = csv.shape[0]
    print(arabic_sentences.shape, csv.shape)
    # print(csv.at[0, 1])
    pos = 0
    ids = []
    sentences = []
    for i in range(0, rows):
        arabic_id = arabic_sentences.at[i, "ID"]
        for j in range(0, csv_len):
            audio_id = csv.at[j, 0]
            if audio_id == arabic_id:
                # sav
                print(arabic_sentences.at[i, "sentences"])
                ids.append(arabic_id)
                sentences.append(arabic_sentences.at[i, "sentences"])

    dictionary = {
        "ids": ids,
        "sentences": sentences
    }

    df = pd.DataFrame(data=dictionary)
    df.to_csv("arabic_sentencs_with_audio.csv")

audios2()
# path = "/mnt/c/Users/Ameen/Development/data/en/clips/"
