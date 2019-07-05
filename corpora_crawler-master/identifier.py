import glob
import os

from helpers.language_identifier import Identifier
from helpers.config import DOCS_TO_PROCESS_PATH, PROBABLE_DOCS_PER_LANGUAGE_PATH, DOCS_PROCESSED_PATH
from helpers.logger import Logger
from helpers.utils import create_file, add_to_language_assets


log = Logger()


def sum_probabilities(probabilities):
    """
    Given a list of {
      'lang_1': XX%,
      'lang_2': XX%,
      'lang_3': XX%,
    }
    returns the sum of all probabilities for each language as {
      'lang_1': sum_lang_1%,
      'lang_2': sum_lang_2%,
      'lang_3': sum_lang_3%,
    }
    """
    result = {}
    for probability in probabilities:
        for key in probability.keys():
            if key not in result.keys():
                result[key] = 0
            result[key] = result[key] + probability[key]
    return result


def average_probabilities(probabilities):
    """
    Given a list of {
      'lang_1': XX%,
      'lang_2': XX%,
      'lang_3': XX%,
    }
    returns the average probability for each language as {
      'lang_1': average_lang_1%,
      'lang_2': average_lang_2%,
      'lang_3': average_lang_3%,
    }
    """
    result = sum_probabilities(probabilities)
    occurrences = {}
    for probability in probabilities:
        for key in probability.keys():
            if key not in occurrences.keys():
                occurrences[key] = 0
            occurrences[key] = occurrences[key] + 1
    for key in result.keys():
        result[key] = result[key] / occurrences[key]
    return result


def probability_criteria_check(percentage):
    return percentage > 40


def save_text(filename, text, probability):
    """
    if the probability for the most probable language is higher than 40%
    then save the file to that language folder
    """
    if probability.items():
        most_probable = max(probability.items(), key=lambda k: k[1])
        language_slug = most_probable[0]
        if probability_criteria_check(most_probable[1]):
            file_path = f"{PROBABLE_DOCS_PER_LANGUAGE_PATH}{language_slug}/{filename}"
            create_file(file_path)
            with open(file_path, 'w') as f:
                log.info(f"Saving text in '{language_slug}' probable docs folder as '{filename}'")
                f.write(text)
            return 1
    return 0


def add_to_probable_assets(text, probability):
    if probability.items():
        most_probable = max(probability.items(), key=lambda k: k[1])
        language_slug = most_probable[0]
        if probability_criteria_check(most_probable[1]):
            add_to_language_assets(language_slug, text, 'probable-')


def mark_file_as_processed(filename):
    log.info(f"Marking '{os.path.basename(filename)}' as processed")
    new_path = f"{DOCS_PROCESSED_PATH}{os.path.basename(filename)}"
    create_file(new_path)
    os.rename(filename, new_path)


def identify(filenames_path):
    """
    For each paragraph of each file uses our algorithm to
    check the probability of being of all each of the languages we support
    """
    identifier = Identifier(log)
    for filename in filenames_path:
        with open(filename) as f:
            log.info(f"Checking probabilities for '{filename}'")
            file_content = f.read()
            text = list(filter(None, file_content.split('\n')))
            probabilities = []
            i = 0
            for paragraph in text:
                probability = identifier.identify(paragraph)
                probabilities.append(probability)
                i += save_text(f"{os.path.basename(filename)}.{i}", paragraph, probability)
                add_to_probable_assets(paragraph, probability)
            save_text(f"{os.path.basename(filename)}", file_content, average_probabilities(probabilities))
            mark_file_as_processed(filename)


filenames_path = glob.glob(os.path.join(DOCS_TO_PROCESS_PATH, '*.txt'))
identify(filenames_path)
