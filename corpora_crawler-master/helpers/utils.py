# Simple imports
import os
import json
import string
import random
import re
# import nltk

from helpers.config import LANGUAGES_FILE, SPECIAL_CHAR, LANGUAGES_PATH


def create_folder(path):
    """ creates a folder if it does not exists """
    if not os.path.exists(path):
        os.makedirs(path)


def create_file(path, fill=None):
    """ creates a file and all folders that do not exist in the given path """
    try:
        if not os.path.isfile(path):
            with open(path, 'w') as f:
                if fill:
                    f.write(fill)
                f.close()
    except FileNotFoundError:
        folder_path = '/'.join(path.split('/')[0:-1])
        create_folder(folder_path)
        create_file(path, fill)


def get_languages():
    """ retrieves the languages dictionary """
    return load_json_file(LANGUAGES_FILE, [])


def sort_dict_by_value(dictionary):
    """ sorts a dict by value """
    return dict(sorted(dictionary.items(), key=lambda k: -k[1]))


def clean_word(word): # Function that clean all words.  #####Can be better.
    word = ''.join(i for i in word if not i.isdigit()) # Take off digits from the word.
    if len(word):
        if word[-1] in SPECIAL_CHAR: # Take out first letter if is a SPECIAL_CHAR.
            word = word[:-1]
    if len(word):
        if word[0] in SPECIAL_CHAR: # Take out last letter if is a SPECIAL_CHAR.
            word = word[:0]
    return word


def clean_filename(word):
    """ removes all chars except a-zA-Z0-9_ from given word """
    return re.sub('[^A-Za-z0-9_\.]+', '', word)


def random_string(length=16):
    """ generates a random string with default length of 16 """
    letters = string.ascii_lowercase + string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(length))


def load_json_file(filename, default={}):
    create_file(filename)
    with open(filename, 'r') as f:
        try:
            return json.load(f)
        except Exception:
            pass
    return default


def save_json_file(filename, dictionary):
    create_file(filename)
    with open(filename, 'w') as f:
        try:
            f.write(json.dumps(dictionary, indent=4))
            return True
        except Exception:
            return False


def split_text(text):
    # words = nltk.word_tokenize(text)
    return text.split()


def get_words_relations(text, data={}):
    words = split_text(text)
    prev_word = ''
    for word in words:
        word = clean_word(word)
        if word:
            if not (word in data.keys()):
                data[word] = {
                    'prev': {},
                    'next': {},
                    'occurrences': 0
                }
            data[word]['occurrences'] = data[word]['occurrences'] + 1
            if prev_word:
                if not (prev_word in data[word]['prev'].keys()):
                    data[word]['prev'][prev_word] = 0
                data[word]['prev'][prev_word] = data[word]['prev'][prev_word] + 1
                if not (prev_word in data.keys()):
                    data[prev_word] = {
                        'prev': {},
                        'next': {},
                        'occurrences': 0
                    }
                data[prev_word]['occurrences'] = data[prev_word]['occurrences'] + 1
                if not (word in data[prev_word]['next'].keys()):
                    data[prev_word]['next'][word] = 0
                data[prev_word]['next'][word] = data[prev_word]['next'][word] + 1
            prev_word = word
    return data


def add_to_language_assets(language_slug, text, prefix=''):
    language_dict_path = f"{LANGUAGES_PATH}{language_slug}/{prefix}dictionary.json"
    words_dict_path = f"{LANGUAGES_PATH}{language_slug}/{prefix}words_list"
    create_file(language_dict_path)
    create_file(words_dict_path)
    with open(language_dict_path, 'r') as f:
        try:
            data = json.load(f)
        except Exception:
            data = {}
    language_dict = get_words_relations(text, data)
    with open(words_dict_path, 'w') as f:
        f.write('\n'.join(sorted(set(language_dict.keys()))))
    with open(language_dict_path, 'w') as f:
        f.write(json.dumps(language_dict, indent=4))
