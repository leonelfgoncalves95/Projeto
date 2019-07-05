import os
import glob

from helpers.utils import get_languages, add_to_language_assets, create_file
from helpers.config import BOOTSTRAP_PATH
from helpers.logger import Logger


log = Logger()

data = {}


def process_language_bootstrap_files(language):
    base_path = f"{BOOTSTRAP_PATH}{language['slug']}/"
    files = glob.glob(os.path.join(base_path, '*.txt'))
    log.info(f"Boostraping '{language['slug']}' language with {files}")
    if files:
        for filename in files:
            with open(filename, 'r') as f:
                log.info(f"Adding '{os.path.basename(filename)}' words to '{language['slug']}' language assets")
                add_to_language_assets(language['slug'], f.read())
            folder_path, name = os.path.split(filename)
            new_path = f"{folder_path}/processed/{name}"
            create_file(new_path)
            os.rename(filename, new_path)
    else:
        log.warning(f"There is no files to add to '{language['slug']}' language assets")


languages = get_languages()
for language in languages:
    process_language_bootstrap_files(language)
