# Simple imports

# External imports

# Internal imports
from helpers.config import LANGUAGES_PATH
from helpers.query import Query
from helpers.utils import create_folder, create_file, load_json_file


class LanguageProcessor:
    language_slug = ''
    language_names = []
    language_path = ''
    dictionary_path = ''
    dictionary = {}
    words_list = set()

    def __init__(self, language, log, *args, **kwargs):
        self.log = log
        self.language_slug = language.get('slug', '')
        self.language_names = language.get('names', [])
        self.base_path = self._get_language_path(self.language_slug)
        self.dictionary_path = f"{self.base_path}dictionary.json"
        self.words_list_path = f"{self.base_path}words_list"
        self._create_language_assets(self.base_path)
        self.dictionary = self.get_dictionary()
        self.words_list = self.get_words_list()

    def get_dictionary(self):
        return load_json_file(self.dictionary_path)

    def get_words_list(self):
        try:
            with open(self.words_list_path, 'r') as f:
                return f.read().split()
        except Exception as e:
            self.log.error(e)
        return []

    def query(self, times, pages, min_words, max_words):
        results = []
        if not self.is_empty():
            q = Query(
                self.log, self.language_slug, self.words_list, self.dictionary, times, pages, min_words, max_words
            )
            results = q.get_results()
        return results

    def is_empty(self):
        return len(self.words_list) == 0

    def _get_language_path(self, slug):
        return f"{LANGUAGES_PATH}{slug}/"

    # The files created for each language are:
    #   * dictionary.json
    #   * words_list
    def _create_language_assets(self, path):
        create_folder(path)
        create_file(f"{path}dictionary.json", '{}')
        create_file(f"{path}words_list")
