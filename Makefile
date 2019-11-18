SOURCE ?=/Users/aravindkumar/FILE/Source
DESTINATION ?=/Users/aravindkumar/FILE/Destination

.DEFAULT_GOAL := explain
explain:
	### Welcome
    # Makefile for the Python Folder Sync Application
	#
	#
	### Installation
	#
	# Install Python Dependencies for the Project
	#  -> $$ make install-python-deps
	#
	#
	### Sync Folders
	#
	# To start Sync
	#  -> $$ make sync
	#
	#  Note: Make sure you have provided the necessary parameters in MAKEFILE
	#
	#
	### Targets
	#
	@cat Makefile* | grep -E '^[a-zA-Z_-]+:.*?## .*$$' | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: install-python-deps
install-python-deps: ## Install Python Dependencies
	pip3 install -r requirements.txt

.PHONY: sync
sync: ## start Sync
	python3 sync.py -src=$(SOURCE) -dest=$(DESTINATION)
