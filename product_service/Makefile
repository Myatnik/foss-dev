.PHONY: create-structure install-dep install test-pytest test build-app run

create-structure:
	if not exist src mkdir src
	if not exist tests mkdir tests
	if not exist docs mkdir docs
	type nul > src/.gitkeep
	type nul > tests/.gitkeep
	type nul > docs/DOMAIN.md
	type nul > README.md
	type nul > .gitignore
	type nul > setup.py
	type nul > requirements.txt

install-dep:
	python -m pip install -r requirements.txt

install:
	python -m pip install -e .

test-pytest:
	python -m pytest

test: install-dep install test-pytest

build-app:
	docker build -t product_service:dev .

run:
	docker run --rm --name product-service -p 8001:8000 product_service:dev
