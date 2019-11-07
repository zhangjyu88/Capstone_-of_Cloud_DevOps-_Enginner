#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

# Assumes that an image is built via `run_docker.sh`

# Step 1:
# Create dockerpath
# dockerpath=<your docker ID/path>
dockerpath=bostonhouseflasktest
dockertag=v1.0
dockeruser=zhangjyu

# Step 2:  
# Authenticate & tag
echo "Docker ID and Image: $dockerpath:$dockertag"

docker tag $dockerpath:latest $dockeruser/$dockerpath:$dockertag
# Step 3:
# Push image to a docker repository
docker push $dockeruser/$dockerpath:$dockertag