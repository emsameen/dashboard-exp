#!/bin/bash

# Set the Docker image name
IMAGE_NAME="grafana-image"

# Build the Docker image
docker build -t $IMAGE_NAME .

# Start the Grafana container with the name "grafana"
docker run -d -p 3000:3000 --name grafana $IMAGE_NAME
