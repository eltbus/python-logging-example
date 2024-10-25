build:
	@docker build -t mini-app .

build-alt:
	@docker build --build-arg logging_config_file="./alt_logging_config.yaml" -t mini-app .

run:
	@docker run --rm -t -p 8000:8000 mini-app

check-concurrency:
	@for i in {1..3}; do \
        curl -sX 'GET' localhost:8000 -o /dev/null & \
        sleep .5; \
    done
