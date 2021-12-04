# ecs-logs

## Create ECR repo

```bash
aws ecr create-repository \
    --repository-name python-hello-world
```

## Docker build and push

```bash
# Retrieve an authentication token and authenticate your Docker client to your registry.
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 777252479890.dkr.ecr.us-east-1.amazonaws.com

# Build your Docker image.
docker build -t python-hello-world .

# Tag your image so you can push the image to this repository.
docker tag python-hello-world:latest 777252479890.dkr.ecr.us-east-1.amazonaws.com/python-hello-world:latest

# push this image to AWS repository
docker push 777252479890.dkr.ecr.us-east-1.amazonaws.com/python-hello-world:latest
```
