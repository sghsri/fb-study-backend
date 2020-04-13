define USAGE
Apply.fyi backend

Commands:
	init      Setup virtual environment and packages
	run       activate venv and run
	debug     set debug flag
	clean	  clean up the app for
endef

export USAGE
help:
	@echo "$$USAGE"

init:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip3 install -r requirements.txt; \

run:
	. venv/bin/activate; \
	export FLASK_APP=main.py; \
	flask run; \

debug:
	export FLASK_ENV=development

clean:
	rm -rf venv; \
    find -iname "*.pyc" -delete; \
