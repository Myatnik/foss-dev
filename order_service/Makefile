.PHONY: create-structure install-dep install test-pytest test run build-app run-docker

SHELL := powershell.exe
.SHELLFLAGS := -NoProfile -Command

create-structure:
	New-Item -ItemType Directory -Force -Path src, tests, docs | Out-Null
	New-Item -ItemType File -Force -Path src\.gitkeep, tests\.gitkeep | Out-Null
	New-Item -ItemType File -Force -Path docs\DOMAIN.md, README.md, .gitignore, setup.py, requirements.txt | Out-Null

install-dep:
	python -m pip install -r requirements.txt

install:
	python -m pip install -e .

test-pytest:
	python -m pytest tests/ -v

test: install-dep install test-pytest

run:
	py -m poetry install
	py -m poetry run uvicorn app.main:app --host 127.0.0.1 --port 8002

build-app:
	docker build -t product_service:dev ./

run-docker:
	docker run --rm --name order-service -p 8002:8000 order_service:dev