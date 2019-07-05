# External imports
from bs4 import BeautifulSoup

# Internal imports
from helpers.processors.base_processor import BaseProcessor


class TEXT_Processor(BaseProcessor):
    def file_to_text(self):
        with open(self.original_path, 'r') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            return soup.get_text()
