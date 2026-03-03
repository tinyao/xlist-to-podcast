.PHONY: setup generate generate-force

setup:
	pip install -r requirements.txt

generate:
	python -m generate

generate-force:
	python -m generate --force
