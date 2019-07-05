# Simple imports
import requests

# Internal imports
from helpers.processors.docx_processor import DOCX_Processor
from helpers.processors.pdf_processor import PDF_Processor
from helpers.processors.html_processor import HTML_Processor
from helpers.processors.text_processor import TEXT_Processor


class FileProcessor:
    processor_dictionary = {
        'application/msword': DOCX_Processor,
        'application/pdf': PDF_Processor,
        'text/html': HTML_Processor,
        'text/plain': TEXT_Processor
    }

    def __init__(self, url, log, *args, **kwargs):
        self.url = url
        self.log = log
        self.content_type = self.get_content_type(url)

    def get_content_type(self, url):
        try:
            r = requests.get(url)
            return r.headers.get('content-type')
        except Exception as e:
            self.log.error(e)
        return False

    def process(self):
        processable = False
        if self.content_type:
            for content_type in self.processor_dictionary.keys():
                if content_type in self.content_type:
                    processable = True
                    self.processor_dictionary[content_type](self.log, self.url, content_type)
        if not processable:
            self.log.warning(f"There is no processor for content_type: '{self.content_type}'")
