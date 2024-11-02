.PHONY: build run shell clean

# Docker image name
IMAGE_NAME = steve-jobs-py
CONTAINER_NAME = steve-jobs-py-container

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm -it \
		--name $(CONTAINER_NAME) \
		-v $(PWD):/app \
		$(IMAGE_NAME)

shell:
	docker run --rm -it \
		--name $(CONTAINER_NAME) \
		-v $(PWD):/app \
		$(IMAGE_NAME) /bin/bash

clean:
	docker rm -f $(CONTAINER_NAME) 2>/dev/null || true
	docker rmi -f $(IMAGE_NAME) 2>/dev/null || true
