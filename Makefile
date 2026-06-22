# Variables
PYTHON = python
MANAGE = $(PYTHON) manage.py

.PHONY: help install run test clean migrations

help:
	@echo "Available commands:"
	@echo "  make install    - Install dependencies"
	@echo "  make run        - Start the Django development server"
	@echo "  make test       - Run all tests (dashboard and apps)"
	@echo "  make migrations - Create and apply database changes (SQLite)"
	@echo "  make clean      - Remove bytecode and the SQLite database"

all: install test clean

install:
	pip install -r requirements.txt

run:
	$(MANAGE) runserver

test:
	$(MANAGE) test

migrations:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

clean:
	-find . -type d -name "__pycache__" -exec rm -rvf {} \;
	-find . -type d -name ".DS_Store" -exec rm -rvf {} \;
	-rm -f db.sqlite3
