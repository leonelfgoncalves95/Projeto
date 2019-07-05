# Simple imports
import os

# Internal imports
from helpers.utils import create_file
from helpers.processors.base_processor import BaseProcessor


class PDF_Processor(BaseProcessor):
    def get_file_name(self):
        name = super().get_file_name()
        return f"{name}.pdf"

    def file_to_text(self):
        provisory_file_name = f"/tmp/processor-provisory/{self.name}.txt"
        create_file(provisory_file_name)
        bashCommand = f"pdftotext -layout {self.original_path} {provisory_file_name}"
        os.system(bashCommand)
        with open(provisory_file_name, 'r') as f:
            return f.read()
        return ''
