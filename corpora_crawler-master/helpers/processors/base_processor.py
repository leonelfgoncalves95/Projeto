import requests

from urllib.parse import urlparse

from helpers.config import DOCS_TO_PROCESS_PATH
from helpers.utils import clean_filename, create_file, random_string


class BaseProcessor:
    def __init__(self, log, url, content_type, *args, **kwargs):
        self.log = log
        self.url = url
        self.parsed_url = urlparse(url)
        self.name = self.get_file_name()
        self.content_type = content_type
        self.extension = self.content_type.split('/')[-1]
        self.log.info(f"Processing '{self.url}' as '{self.content_type}'")
        self.extract_text()

    def get_file_name(self):
        return clean_filename(f"{self.parsed_url.netloc}__{random_string(16)}")

    def get_file(self):
        self.log.info(f"Downloading '{self.name}' from '{self.url}'")
        self.request = requests.get(self.url)

    def save_file(self, text=None):
        self.log.info(f"Saving '{self.name}' from '{self.url}'")
        self.original_path = f"{DOCS_TO_PROCESS_PATH}{self.extension}/{self.name}"
        self.txt_path = f"{DOCS_TO_PROCESS_PATH}{self.name}.txt"
        create_file(self.original_path)
        with open(self.original_path, 'wb') as f:
            f.write(self.request.content)

    def save_text_file(self, text):
        self.log.info(f"Converting '{self.name}' to '{self.name}.txt'")
        create_file(self.txt_path)
        with open(self.txt_path, 'w') as f:
            text = f"{self.url}\n\n\n\n{text}"
            f.write(text)

    def file_to_text(self):
        raise NotImplementedError()

    def extract_text(self):
        self.get_file()
        self.save_file()
        try:
            text = self.file_to_text()
            self.save_text_file(text)
        except Exception as e:
            self.log.info(e)
