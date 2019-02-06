import glob
import math
import os

import pandas as pd
from jiwer import wer
from pydub import AudioSegment
from sklearn.feature_extraction.text import TfidfVectorizer

from transcription_analysis import engine

audio_folder_path = "/development/dataset/cv_corpus_v1/"
audio_transcription_excel = "/development/dataset/cv_corpus_v1/cv-valid-dev.csv"
transcription_path = "/development/pycharm/audio_analysis/audio_files/transcription/"


# iterate over the test data and then combine all the audios which resides there into a large audio file
def combine_audios(audio_num, path, excel_file=audio_transcription_excel, audio_folder_path=audio_folder_path):
    # Get all the mp3 files in the audio_folder_path and store them in results. Sort them by name
    results = [os.path.basename(f) for f in glob.glob(os.path.join(audio_folder_path,"*.mp3"))]

    # Read the excel file
    excel = pd.read_csv(excel_file)
    excel_values = excel.values

    audio_files = []
    # get the files names of audios with only english or canadian accent
    for index in range(len(excel_values)):
        if excel_values[index][6] == "us" or excel_values[index][6] == "canada":
            audio_files.append(excel_values[index][0])

    audio_files.sort()

    # combine audio files from short audios to a little longer audios
    combined_audio = AudioSegment.empty()
    for index in range(len(audio_files)):
        filename = audio_files[index]

        current_audio = AudioSegment.from_mp3(audio_folder_path + filename)

        if (index + 1) % audio_num == 0:
            print(index + 1)
            output_file = combined_audio.export(path + "sample_" + str(index + 1) + ".mp3"
                                                , format="mp3")
            output_file.close()
            combined_audio = AudioSegment.empty()

        # update
        second_of_silence = AudioSegment.silent(duration=100)
        combined_audio = combined_audio + second_of_silence + current_audio


def generate_actual_transcription(num, excel_file, output_path):
    # Read the excel file
    excel = pd.read_csv(excel_file)
    excel_values = excel.values

    audios = {}
    # get the files names of audios with only english or canadian accent
    for index in range(len(excel_values)):

        if excel_values[index][6] == "us" or excel_values[index][6] == "canada":
            audios[excel_values[index][0]] = excel_values[index][1]

    audio_files = []
    for key in audios.keys():
        audio_files.append(key)

    audio_files.sort()

    current_text = ""
    for index in range(len(audio_files)):
        if (index + 1) % num == 0:
            # write current_text into a file
            with open(output_path + "sample_" + str(index + 1) + ".txt", "w") as text_file:
                text_file.write(current_text)
            # Empty the text
            current_text = ""

        current_text += (" " + audios[audio_files[index]])


def change_name(path, ext):
    results = [os.path.basename(f) for f in glob.glob(os.path.join(path, ext))]
    for index in range(len(results)):
        os.rename(path + results[index], path + results[index].split("sample_")[1])


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


# analyze accuracy of transcribed txt and actual transcription
def analyze_accuracy():
    actual_path = "/actual/short/us+canada/"
    generated_path = "/generated/short/us+canada/"

    results = [os.path.basename(f) for f in glob.glob(os.path.join(transcription_path + actual_path,"*.txt"))]

    score = 0
    for index in range(len(results)):
        with open(transcription_path + actual_path + results[index], 'r') as current_file:
            actual_text = current_file.read().replace('\n', '')

        with open(transcription_path + generated_path + results[index], 'r') as current_file:
            generated_text = current_file.read().replace('\n', '')

        score += get_similarity_score(actual_text, generated_text)
        print(index, results[index], get_similarity_score(str(actual_text).split(),
                                                          generated_text).split())

    return float(score / len(results))


def create_db_from_csv(excel_path=audio_folder_path):
    import csv
    import sqlite3

    con = sqlite3.Connection('output.sqlite')
    cur = con.cursor()
    cur.execute('drop table "transcription"')
    cur.execute('CREATE TABLE "transcription" ("id" integer, "filename" text, "text" text, '
                '"duration" real, "google_transcriptionUS" text, "similarityScore" real, '
                '"up_votes" integer, "down_votes" integer, "age" text, "gender" text, "accent" text);')

    f = open(excel_path + 'cv-valid-dev.csv')
    csv_reader = csv.reader(f)

    print (csv_reader)
    cur.executemany('INSERT INTO transcription VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', csv_reader)
    cur.close()
    con.commit()
    con.close()
    f.close()


# transcribe all the audios using the en-US modal
def transcribe_audios2(file_path=audio_folder_path, excel_file=audio_transcription_excel):
    # Read the excel file
    excel = pd.read_csv(excel_file)
    excel_values = excel.values

    for index in range(0, len(excel_values)):
        transcription = engine.transcribe_any_audio(file_path + excel_values[index][0], "en-US")
        actual = excel_values[index][1]
        score = get_similarity_score(transcription, actual)

        print(index)
        print("actual: ", actual)
        print("generated: ", transcription)
        print(score)

        excel.at[index, 'google_transcriptionUS'] = transcription
        excel.at[index, 'similarityScore'] = score

        # Save regularly
        if index % 10 == 0:
            excel.to_csv(file_path + "/cv-valid-dev.csv")

        # if result < 0.7:
        #     error.append(key)

    excel.to_csv(file_path + "/cv-valid-dev.csv")


# transcribe and calculate the word error rate for audios with blank transcription within the US transcription
def transcribe_audios_that_were_not_transcribed(file_path=audio_folder_path):

    # Read the excel file
    excel = pd.read_csv("./updated_cv_valid_dev.csv", dtype='str')
    excel_values = excel.values
    counter = 0

    # get the files names of audios with only english or canadian accent
    for index in range(0, len(excel_values)):
        accent = excel.at[index, 'google_transcriptionUS']
        if type(accent) != str and math.isnan(accent):
            actual = excel.at[index, 'text']
            transcription = engine.transcribe_any_audio(file_path + excel.at[index, 'filename'], 'en_IN')
            score = get_similarity_score(actual, transcription)
            error = wer(str(actual), str(transcription))
            # Display
            print(counter, excel.at[index, 'filename'])
            print("actual: ", actual)
            print("generated: ", transcription)
            print(score, 1 - error)
            # Store
            excel.at[index, 'similarityScore_india'] = str(score)
            excel.at[index, 'word_error_rate_india'] = str(1 - error)
            excel.at[index, 'google_transcriptionIndia'] = transcription

            # Regularly Save
            if counter % 10 == 0:
                excel.to_csv("output.csv")
            counter = counter + 1

        excel.to_csv("output.csv")


# transcribe and calculate the word error rate
def transcribe_audios_using_their_accent_modal(accent, modal_code, file_path=audio_folder_path):
    from jiwer import wer
    # Read the excel file
    excel = pd.read_csv("./updated_cv_valid_dev.csv", dtype='str')

    excel_values = excel.values
    counter = 0
    # get the files names of audios with only english or canadian accent
    for index in range(0, len(excel_values)):
        actual_accent = excel.at[index, 'accent']
        if actual_accent == accent:
            actual = excel.at[index, 'text']
            transcription = engine.transcribe_any_audio(file_path + excel.at[index, 'filename'], modal_code)

            score = get_similarity_score(actual, transcription)
            error = wer(str(actual), str(transcription))
            # display
            print(counter, excel.at[index, 'filename'])
            print("actual: ", actual)
            print("generated: ", transcription)
            print(score, 1 - error)
            # Store
            excel.at[index, 'similarityScore_india'] = str(score)
            excel.at[index, 'word_error_rate_india'] = str(1 - error)
            excel.at[index, 'google_transcriptionIndia'] = transcription

            # Regularly save
            if counter % 10 == 0:
                excel.to_csv("output.csv")
            counter = counter + 1

    excel.to_csv("output.csv")


def transcribe_using_deep_speech():
    pass


# Transcribe audios and translate file. Store the result into a csv file
def transcribe_audios(file_paths, format="mp3", modal_code="en-US"):
    # Get result from the engine transcription
    audio_files = [os.path.basename(f) for f in glob.glob(os.path.join(file_paths, '*.' + format))]
    audio_files.sort()

    transcription_output = []
    translation_output = []
    files = []
    for index in range(len(audio_files)):
        transcription = engine.transcribe_any_audio(file_paths + audio_files[index], modal_code)
        transcription_output.append(transcription)
        translation = engine.translate_text_from(transcription, modal_code.split("-")[0])
        translation_output.append(translation['translation'])
        files.append(audio_files[index].split(format)[0])

        print(audio_files[index], transcription, translation['translation'])

    output_dictionary = {"files": files,
                         "transcription_" + modal_code: transcription_output,
                         "translation_" + modal_code: translation_output
                         }
    df = pd.DataFrame(data=output_dictionary)
    df.to_csv("transcription_output_" + modal_code + ".csv")


def pre_process_arabic_string(str):
    from lang_trans.arabic import buckwalter
    import re
    # Remove all non alphabitic symbols
    output = buckwalter.trans(re.sub(r'([^\s\w]|_)+', '', str))
    # Remove all symbols
    reg = re.compile('[aui~oFNK]')
    output = reg.sub('', output)

    # Replace different shapes of alf into a single one
    reg = re.compile('[|><]')
    output = reg.sub('A', output)

    # Convert the string back
    return buckwalter.untrans(output)


# transcribe all the audios using the en-US modal
def add_scores_into_csv(excel_file, actual_col, generated_col):
    # Read the excel file
    excel = pd.read_csv(excel_file)
    excel_values = excel.values

    for index in range(0, len(excel_values)):
        actual = pre_process_arabic_string(excel.at[index, actual_col])
        generated = pre_process_arabic_string(excel.at[index, generated_col])

        # score = get_similarity_score(str(actual), str(generated))
        word_er = wer(str(actual), str(generated))
        word_er = 1 if word_er > 1 else word_er
        excel.at[index, "word_error_rate"] = 1 - word_er

        print("actual: ", actual)
        print("generated: ", generated)
        print(1 - word_er)

    excel.to_csv(excel_file)


path = "/home/ameen/development/pycharm/audio_analysis/transcription_performance_test/"
add_scores_into_csv(path + "transcription_output_ar-QA.csv", "actual_text", "transcription_ar-QA")

transcribe_using_deep_speech()
# transcribe_audios("/home/ameen/development/dataset/arabic_audio/", format="wav", modal_code="ar-QA")
