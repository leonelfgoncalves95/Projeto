# External imports
from bs4 import BeautifulSoup

# Internal imports
from helpers.processors.base_processor import BaseProcessor


class HTML_Processor(BaseProcessor):
    def get_file_name(self):
        name = super().get_file_name()
        return f"{name}.html"

    def file_to_text(self):
        with open(self.original_path, 'r') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            self.extract_media_content(soup)
            text_list = []
            for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']:
                for text_tags in soup.find_all(tag):
                    text_list.append(text_tags.text)
            return '\n\n'.join(text_list)
        return ''

    def extract_media_content(self, soup):
        """
        TODO: Implement
        download video as mp3 if youtube -> https://thenoobsway.com/how-to-download-a-youtube-video-and-convert-it-into-mp3-using-python/
        extract videos and audios from html and save all as mp3
        """
