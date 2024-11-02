.PHONY: build run shell clean

IMAGE_NAME = steve-jobs-app
CONTAINER_NAME = steve-jobs-container

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm -it \
		--name $(CONTAINER_NAME) \
		-v $(PWD):/app \
		$(IMAGE_NAME)

run-dev:
	docker run --rm -it \
		--name $(CONTAINER_NAME) \
		-v $(PWD):/app \
		$(IMAGE_NAME) python src/main.py

shell:
	docker run --rm -it \
		--name $(CONTAINER_NAME) \
		-v $(PWD):/app \
		$(IMAGE_NAME) /bin/bash

clean:
	docker rm -f $(CONTAINER_NAME) 2>/dev/null || true
	docker rmi -f $(IMAGE_NAME) 2>/dev/null || true