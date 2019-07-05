# Internal imports
from helpers.utils import get_languages, sort_dict_by_value, clean_word
from helpers.config import LANGUAGES_PATH


class Identifier:
    minimum_words = 10

    def __init__(self, *args, **kwargs):
        self.languages = get_languages()
        self.words_lists = self.open_words_lists()

    def identify(self, text):
        dictionary = {}
        for language in self.languages:
            language_slug = language['slug']
            dictionary[language_slug] = self.language_probability(text, self.words_lists[language_slug])
        return sort_dict_by_value(dictionary)

    def language_probability(self, text, word_list):
        count = 0
        words = text.split(' ')
        length = len(words)
        for word in words:
            word = clean_word(word)
            if word in word_list:
                count += 1
        return count * 100 / max(length, self.minimum_words)

    def open_words_lists(self):
        dictionaries = {}
        for language in self.languages:
            language_slug = language['slug']
            dictionaries[language_slug] = self.get_words_list(language_slug)
        return dictionaries

    def get_words_list(self, language_slug):
        words_list_path = f"{LANGUAGES_PATH}{language_slug}/words_list"
        try:
            with open(words_list_path, 'r') as f:
                return f.read().split()
        except Exception as e:
            self.log.error(e)
        return []
