IMAGE_NAME := my_fastapi_app

.PHONY: build run

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -d -p 8000:8000 $(IMAGE_NAME)

stop:
	docker stop $$(docker ps -q --filter ancestor=$(IMAGE_NAME))

clean:
	docker system prune -f