# Makefile

help:
	@echo " "
	@echo "install - installs requirements from requirements.text"
	@echo "run - starts flask application"
	@echo "dbinit - initialize database migrations"
	@echo "dbup - database upgrade (db upgrade)"
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


## Run flask app
run:
	flask run


## DB Management
dbinit:
	flask db init
dbup:
	flask db upgrade



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