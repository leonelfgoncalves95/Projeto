# Simple imports
import fulltext

# Internal imports
from helpers.processors.base_processor import BaseProcessor


class DOCX_Processor(BaseProcessor):
    def get_file_name(self):
        name = super().get_file_name()
        return f"{name}.doc"

    def file_to_text(self):
        return fulltext.get(self.original_path, '')
