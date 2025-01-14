.PHONY: setup update fmt check

PM=python manage.py

setup:
	poetry install

update:
	poetry update

fmt:
	autoflake --recursive --remove-all-unused-imports --in-place . && isort . && black .
	echo "fmt django templates"

fmt-templates:
	djlint --reformat templates/

check:
	isort --check .
	black  --check .

runserver:
	$(PM) runserver 0.0.0.0:8000

migrate:
	$(PM) migrate

migrations:
	$(PM) makemigrations

shell:
	$(PM) shell
