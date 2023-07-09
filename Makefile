.DEFAULT_GOAL: usage
.PHONY: usage install build run lint test

# Variables
LOG_DIR = logs
$(LOG_DIR):
	@mkdir -p $(LOG_DIR)

BACKUP_DIR = backups
$(BACKUP_DIR):
	@mkdir -p $(BACKUP_DIR)

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
run: | $(LOG_DIR) $(BACKUP_DIR)
	@poetry run python openct

# Run Pylint
lint:
	@poetry run pylint --rcfile .pylintrc --recursive=y openct

# Run PyTest
test:
	@poetry run pytest
