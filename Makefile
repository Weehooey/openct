.DEFAULT_GOAL = usage
.PHONY: usage install build run lint test full-monty

# Variables
LOG_DIR = logs
$(LOG_DIR):
	@mkdir -p $(LOG_DIR)

BACKUP_DIR = backups
$(BACKUP_DIR):
	@mkdir -p $(BACKUP_DIR)

DATASTORE_DIR = datastore
$(DATASTORE_DIR):
	@mkdir -p $(DATASTORE_DIR)

CONFIG_DIR = config
$(CONFIG_DIR):
	@mkdir -p $(CONFIG_DIR)

CONFIG_FILE = $(CONFIG_DIR)/config.yml
$(CONFIG_FILE): | $(CONFIG_DIR)
	@poetry run python openct/config

# Targets
usage:
	@echo "Usage: make [target]"

# install dependencies
install: ~/.bash_completion
	@poetry config virtualenvs.in-project true
	@poetry install
	@echo install complete

~/.bash_completion:
	poetry completions bash >> ~/.bash_completion

# build
build:
	@poetry build
	@echo build complete

# Run
run: | $(LOG_DIR) $(BACKUP_DIR) $(DATASTORE_DIR) $(CONFIG_FILE)
	@poetry run python openct

# Run Pylint
lint:
	@poetry run pylint --rcfile .pylintrc --recursive=y openct

# Run PyTest
test:
	@poetry run pytest

full-monty: test lint
	@echo Do both PyTest and Pylint before commit.