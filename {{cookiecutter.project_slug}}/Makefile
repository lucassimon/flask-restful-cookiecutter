.PHONY: help clean test clean-build isort run

.DEFAULT: help

help:
	@echo "make clean:"
	@echo "       Removes all pyc, pyo and __pycache__"
	@echo ""
	@echo "make clean-build:"
	@echo "       Clear all build directories"
	@echo ""
	@echo "make setup_dev"
	@echo "       Install dev dependencies and flake8 webhook"
	@echo "       Needs virtualenv activated and git initalized"
	@echo ""
	@echo "make clone-dotenv"
	@echo "       Creates .env file base on .env-example"
	@echo "       Used by setup_dev command"
	@echo ""
	@echo "make setup"
	@echo "       Install prod dependencies"
	@echo "       Needs virtualenv activated and git initalized"
	@echo ""
	@echo "make isort:"
	@echo "       Run isort command cli in development features"
	@echo ""
	@echo "make lint:"
	@echo "       Run lint"
	@echo ""
	@echo "make coverage:"
	@echo "       Run tests with coverage and generate a badge (svg)"
	@echo ""
	@echo "make test:"
	@echo "       Run tests with coverage, lint, and clean commands"
	@echo ""
	@echo "make dev:"
	@echo "       Run the dev web application, with tests and coverage"
	@echo ""
	@echo "make run:"
	@echo "       Run the web application without tests"
	@echo ""

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . | grep -E "__pycache__|.pytest_cache|.pyc|.DS_Store$$" | xargs rm -rf

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

clone-dotenv:
	@echo "---- Clone dotenv ----"
	@cp .env-example .env
	@echo "---- Finish clone ----"


setup_dev: clone-dotenv
	@echo "---- Installing Python dev dependencies ----"
	@poetry install

coverage: clean test
	@echo "---- Create coverage ----"
	@coverage html -d htmlcov
	@coverage-badge > static/coverage.svg

isort:
	sh -c "isort --skip-glob=.tox --recursive apps/ "


pycodestyle:
	@pycodestyle apps/

pylint:
	@pylint apps/

lint:
	@echo "---- Linter ----"

test:
	@pytest --verbose --cov=apps --color=yes tests/

dev: lint test
	python application.py

run:
	python application.py
