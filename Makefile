# Variables

HOST_PORT = 8000
CNTR_PORT = 8000
TAG = v1.0
NAME = team_tmd_app
REPO_HOST = 680546755927.dkr.ecr.us-east-2.amazonaws.com/opp-app
TAGGED_IMAGE = $(REPO_HOST):$(TAG)

# Build the Docker image 

image: Dockerfile
	docker build -t $(TAGGED_IMAGE) .

run-app-local:
	docker run --detach --publish $(HOST_PORT):$(CNTR_PORT) --name $(NAME) team_tmd_image:latest

run-app-prod:
	docker run --detach --publish $(HOST_PORT):$(CNTR_PORT) --name $(NAME) $(TAGGED_IMAGE)

exec-app:
	docker exec -it $(NAME) bash
