requirements:
	@poetry export --without-hashes --without-urls -o requirements.txt

build:
	@docker build -t mini-app .

build-alt:
	@docker build --build-arg logging_config_file="./alt_logging_config.yaml" -t mini-app .

run:
	@docker run --rm -t -p 8000:8000 mini-app

get:
	@curl -X 'GET' localhost:8000

format:
	@poetry run python -m ruff format main
