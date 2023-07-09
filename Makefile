.DEFAULT_GOAL: usage
.PHONY: usage install build run lint test

# Variables


# Targets
usage:
	@echo "Usage: make [target]"

# install dependencies
install:
	@poetry install
	@echo install complete

# build
build:
	@poetry build
	@echo build complete

# Run
run:
	@python3.11 src/openct

# Run Pylint
lint: | install
	@poetry run pylint --rcfile .pylintrc --recursive=y src

# Run PyTest
test: | install
	@poetry run pytest
