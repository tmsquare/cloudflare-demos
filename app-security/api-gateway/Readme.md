
# Demo setup

Cloudflare API Gateway protects your API from malicious traffic with API Discovery, Schema Validation, mTLS validation, and more. It also helps to maintain high performing APIs with powerful monitoring and management. 

This guide shows how to set up publicly accessible API server, which can be used to test the API Gateway service.

## Prerequisites

 *  Sign up for a Cloudflare Account : `https://dash.cloudflare.com/sign-up`
 *  Install docker: `https://www.docker.com/products/docker-desktop/`
 *  Create a GCP account and login from the terminal: `https://cloud.google.com/sdk/docs/install`
 
We will use `Mockoon` to create our server. Mockoon is a set of free and open-source API mocking tools. (https://mockoon.com/)
The configuration of the server is all defined on the `data.json` file. (feel free to update the endpoints)

## 1 Create the API server container
`Option 1:` Create a new image from scratch
```
# Create the Dockerfile
$ mockoon-cli dockerize --data ./data.json --port 3000 --output ./tmp/Dockerfile

# Build the image
$ cd tmp
$ docker build -t mockoon-image .

# Run the container and test the following endpoints: http://localhost:3000/posts & http://localhost:3000/products
$ docker run -d -p 3000:3000 mockoon-image
```


`Option 2:` Use an existing image from DockerHub
```
# Pull the image from an existing Docker repository
$ docker pull tmsquare/mockoon-image:latest

# Run the container and test the following endpoints: http://localhost:3000/posts & http://localhost:3000/products
$ docker run -d -p 3000:3000 tmsquare/mockoon-image
```

## 2. Deploy the image on GCP
```
# Authenticate and set the project ID
$ gcloud auth login
$ gcloud config set project PROJECT_ID

# Create a Docker repository in Artifact Registry
$ gcloud artifacts repositories create mockoon-docker-repo --repository-format=docker \
    --location=us-west2 --description="Mockoon Docker repository"

# Verify that the repository is created
$ gcloud artifacts repositories list

# Build an image using Dockerfile
$ cd tmp
$ gcloud builds submit --region=us-west2 --tag us-west2-docker.pkg.dev/PROJECT_ID/mockoon-docker-repo/mockoon-image:latest
```


## 3. Create a Cloud Run service to publicly expose the API server
```
gcloud run deploy mockoon-image	\
 --image us-west2-docker.pkg.dev/PROJECT_ID/mockoon-docker-repo/mockoon-image:latest \
 --port='3000' \
 --allow-unauthenticated
```

Wait for the deployment to finish. Upon successful completion, a success message is displayed along with the URL of the deployed service.
