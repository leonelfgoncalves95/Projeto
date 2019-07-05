create_venv:
	if (! [ -d '.venv' ]); then python3 -m venv .venv; fi

activate_venv:
	. .venv/bin/activate

help:
	cat help.txt

install: create_venv
	# sudo apt-get install antiword abiword unrtf poppler-utils libjpeg-dev pstotext
	. .venv/bin/activate && pip3 install -r requirements.txt
	. .venv/bin/activate && pip3 install --user -U -r requirements.txt
	# python3 helpers/install_nltk.py

pipeline: crawler processor identifier

crawler:
	python3 crawler.py

processor:
	python3 processor.py

identifier:
	python3 identifier.py

clean_identifier:
	rm -r docs/identified/
	rm languages/*/probable-dictionary.json
	rm languages/*/probable-word_list

soft_clean:
	rm -r docs

hard_clean: soft_clean
	rm queries.json

initialize:
	python3 bootstrap.py