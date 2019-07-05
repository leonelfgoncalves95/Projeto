# Simple imports
import string

LANGUAGES_PATH = 'languages/'
LANGUAGES_FILE = 'languages.json'
LOG_PATH = 'logs/app.log'
PROVISORY_FILES_PATH = 'tmp/'
DOCS_TO_PROCESS_PATH = 'docs/to_process/'
DOCS_PROCESSED_PATH = 'docs/processed/'
PROBABLE_DOCS_PER_LANGUAGE_PATH = 'docs/identified/'
BOOTSTRAP_PATH = 'bootstrap/'
# Simbolos especiais =>  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~–
SPECIAL_CHAR = string.punctuation + "–" + '—' + "\n" + "\t"
