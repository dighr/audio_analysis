from pydub import AudioSegment
from transcription_analysis import engine
import os
import glob
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

audio_folder_path2 = "/development/dataset/cv_corpus_v1/"
audio_transcription_excel = "/development/dataset/cv_corpus_v1/cv-valid-test.csv"
audio_transcription_excel2 = "/development/dataset/cv_corpus_v1/cv-valid-dev.csv"
transcription_path = "/development/pycharm/audio_analysis/audio_files/transcription/"


# iterate over the test data and then combine all the audios which resides there into a large audio file
def combine_audios(audio_num, path, excel_file=audio_transcription_excel2, audio_folder_path=audio_folder_path2):
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


def transcribe_audios(file_paths, to):
    # Get result from the engine transcription
    results = [os.path.basename(f) for f in glob.glob(os.path.join(file_paths,'*.mp3'))]
    results.sort()

    for index in range(len(results)):
        transcription = engine.transcribe_any_audio(file_paths + results[index], "en-US")
        parts = results[index].split(".")
        with open(to + parts[0] + ".txt", "w") as text_file:
            text_file.write(transcription)


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


def analyze_accuracy(path=transcription_path):
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
        print(index, results[index], get_similarity_score(actual_text, generated_text))

    return float(score / len(results))


# transcribe all the audios
def transcribe_audios2(file_path=audio_folder_path2, excel_file=audio_transcription_excel2):
    # Read the excel file
    excel = pd.read_csv(excel_file)
    excel_values = excel.values

    # get the files names of audios with only english or canadian accent
    # for index in range(2):
    #
    #     if excel_values[index][6] == "us" or excel_values[index][6] == "canada":
    #         audios[excel_values[index][0]] = excel_values[index][1]

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


def create_db_from_csv(excel_path=audio_folder_path2):
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


# call only once
# generate short audio files and store them in the short folder
# combine_audios(6, "../audio_files/short/us+canada/")
# generate long audio files and store them in the long folder
# combine_audios(100, "../audio_files/long/us+canada/")
# generate the actual output
# generate Actual Transcription for the short audios
# enerate_actual_transcription(6, audio_transcription_excel2, "../audio_files/transcription/actual/short/us+canada/")
# generate actual transcription for the long audios
# generate_actual_transcription(100, audio_transcription_excel2, "../audio_files/transcription/actual/long/us+canada/")
# transcribe short audios
# transcribe_audios("../audio_files/short/us+canada/", to="../audio_files/transcription/generated/short/us+canada/")


# change_name("../audio_files/long/", "*.mp3")




