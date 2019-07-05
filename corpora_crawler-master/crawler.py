from helpers.language_processor import LanguageProcessor
from helpers.logger import Logger
from helpers.utils import get_languages


log = Logger()


def crawl(languages):
    for language in languages:
        if language.get('search', True) is not False:
            log.current_language = language['names'][0]
            processor = LanguageProcessor(language, log)
            processor.query(2, 1, 4, 10)
    log.current_language = ''


languages = get_languages()
crawl(languages)
