.PHONY: test
.DEFAULT_GOAL: test

venv:
	python3 -m venv .venv

venv-win:
	python -m venv .venv

venv-activate-win:
	.venv\Scripts\activate.bat

venv-activate:
	source .venv/bin/activate

init:
	pip install -r requirements.txt

code-convention:
	flake8
	pycodestyle