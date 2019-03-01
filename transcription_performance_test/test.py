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
    audio_files = [os.path.basename(f) for f in glob.glob(os.path.join(file_paths, '*.' + format))]
    audio_files.sort()

    transcription_output = []
    translation_output = []
    files = []
    for index in range(len(audio_files)):
        if type == "deepspeech":
            transcription = engine.transcribe_any_audio(file_paths + audio_files[index],
                                                        modal_code, type="deepspeech")
        elif type == "google":
            transcription = engine.transcribe_any_audio(file_paths + audio_files[index], modal_code)

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
    excel = pd.read_csv(excel_file)
    excel_values = excel.values

    for index in range(0, len(excel_values)):
        actual = (excel.at[index, actual_col])
        generated = (excel.at[index, generated_col])

        score = get_similarity_score(str(actual), str(generated))
        word_er = wer(str(actual), str(generated))
        word_er = 1 if word_er > 1 else word_er
        excel.at[index, "word_error_rate"] = 1 - word_er
        excel.at[index, "scores"] = score

        print("actual: ", actual)
        print("generated: ", generated)
        print(1 - word_er)

    excel.to_csv(excel_file)


# transcribe all the audios using the en-US modal
def transcribe_arabic(audio_file_path, transcription_file_path,
                      audio_format='wav', trans_format="lab", modal_code="ar-OM"):
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

        transcription = engine.transcribe_any_audio(audio_file_path + audio_file, modal_code)
        transcription = pre_process_arabic_string(transcription)
        generated_trans.append(transcription)

        with open(transcription_file_path + transcription_files[index], 'r') as file:
            actual = file.read().replace('\n', '')

        actual = buckwalter.untrans(actual)
        actual = pre_process_arabic_string(actual)
        actual_trans.append(actual)

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


path = "/home/ameen/development/pycharm/audio_analysis/transcription_performance_test/"

# transcribe_audios("/home/ameen/development/dataset/arabic_audio/",
#                   format="wav",
#                   modal_code="en-US")


# transcribe_audios("/home/ameen/development/dataset/cv_corpus_v1/cv-valid-dev/",
#                    format="mp3", modal_code="en-US")

add_scores_into_csv(path + "excel/cv-valid-dev.csv", "text", "google_transcriptionUS")
