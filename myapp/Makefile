# Makefile

help:
	@echo " "
	@echo "install - installs requirements from requirements.text"
	@echo "run - starts flask application"
	@echo "dbinit - initialize database migrations"
	@echo "dbup - database upgrade (db upgrade)"
	@echo "build-assets - builds css/js assets"
	@echo "watch-assets - build css/js assets in watch mode"
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo " "

## Install dependencies
.PHONY: install
install:
	@echo "\nInstalling project dependencies from requirements.txt\n"
	pip install -r requirements.txt
	@echo "\nInstalling project dependencies from npm\n"
	npm install
	npm install -D


## Run flask app
run:
	python3 manage.py runserver


## DB Management
dbinit:
	python3 manage.py db init
dbup:
	python3 manage.py db upgrade


## Assets
build-assets:
	python3 manage.py assets build

watch-assets:
	python3 manage.py assets watch


## Cleaning 
clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/