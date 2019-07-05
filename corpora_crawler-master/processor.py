import json

from helpers.logger import Logger
from helpers.file_processor import FileProcessor


log = Logger()
queries = {}


def process_urls(urls):
    for url in urls:
        fp = FileProcessor(url, log)
        fp.process()
        queries['urls'][url] = True


with open('queries.json', 'r') as f:
    queries = json.load(f)
urls = queries.get('urls', {})
urls = filter(lambda x: x[1] is False, urls.items())
if urls:
    urls = dict(urls)
    process_urls(urls.keys())
with open('queries.json', 'w') as f:
    f.write(json.dumps(queries, indent=4))
