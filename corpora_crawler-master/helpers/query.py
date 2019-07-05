# External imports
from google import google
from random import randint, choice

# Internal imports
from helpers.utils import save_json_file, load_json_file


class Query:
    words_list = []
    dictionary = {}

    def __init__(self, log, language_slug, words_list, dictionary, times=10, pages=5, min_words=3, max_words=6):
        self.log = log
        self.language_slug = language_slug
        self.words_list = words_list
        self.dictionary = dictionary
        self.times = times
        self.pages = pages
        self.min_words = min_words
        self.max_words = max_words
        self.queries = self._get_previous_queries()

    def get_results(self):
        results = set()
        for i in range(self.times):
            res = self.ask_google()
            if res is False:
                break
            results.update(res)
        return results

    def ask_google(self):
        phrase = self._get_phrase_from_words_list(self.words_list, self.min_words, self.max_words)
        links = []
        if phrase is False:
            return phrase
        else:
            self.log.info(f"Searching '{phrase}'")
            try:
                search_results = google.search(phrase, self.pages)
            except Exception as e:
                self.log.warning(f"Probably you have exceeded the maximum number of requests ({e})")
                return links
            for result in search_results:
                self._add_result_to_queries(self.language_slug, phrase, result)
                links.append(result.link)
            self._save_queries_to_file(self.queries)
        return links

    def _add_result_to_queries(self, language, phrase, result):
        if language not in self.queries.keys():
            self.queries[language] = {}
        if phrase not in self.queries[language].keys():
            self.queries[language][phrase] = []
        if 'urls' not in self.queries.keys():
            self.queries['urls'] = {}
        if result.link not in self.queries['urls'].keys():
            self.queries['urls'][result.link] = False
        self.queries[language][phrase].append({
            'name': result.name,
            'link': result.link,
            'google_link': result.google_link,
            'description': result.description,
            'thumb': result.thumb,
            'cached': result.cached,
            'page': result.page,
            'index': result.index,
            'number_of_results': result.number_of_results,
        })

    def _save_queries_to_file(self, queries):
        if queries:
            save_json_file('queries.json', queries)

    def _get_previous_queries(self):
        return load_json_file('queries.json')

    def _get_phrase_from_words_list(self, words_list, min_words, max_words):
        phrase = []
        try:
            phrase = []
            i = randint(min_words, max_words)
            while i > 0:
                word = choice(words_list)
                if word:
                    phrase.append(word)
                    i -= 1
            return ' '.join(phrase)
        except Exception as e:
            self.log.error(f"'words_list' is empty ({e})")
        return False
