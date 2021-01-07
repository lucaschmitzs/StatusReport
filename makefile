.PHONY: test
.DEFAULT_GOAL: test

venv:
	virtualenv -p /usr/bin/python3.6 .venv

init:
	pip install -r requirements.txt

code-convention:
	flake8
	pycodestyle