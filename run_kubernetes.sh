#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
dockerpath=zhangjyu/bostonhouseflasktest:v1.0

# Step 2
# Run the Docker Hub container with kubernetes
kubectl run bostonhouseflasktest --port=80 --image=$dockerpath

# Step 3:
# List kubernetes pods
kubectl get pods

# Step 4:
# Forward the container port to a host
kubectl port-forward $(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}') 8000:80
