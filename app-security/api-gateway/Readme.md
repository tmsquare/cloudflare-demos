
# Demo setup

Cloudflare API Gateway protects your API from malicious traffic with API Discovery, Schema Validation, mTLS validation, and more. It also helps to maintain high performing APIs with powerful monitoring and management. 

This guide shows how to set up publicly accessible API server, which can be used to test the API Gateway service.

## Prerequisites

 *  Sign up for a Cloudflare Account : `https://dash.cloudflare.com/sign-up`
 *  Install docker: `https://www.docker.com/products/docker-desktop/`
 *  Create a GCP account and login from the terminal: `https://cloud.google.com/sdk/docs/install`
 
We will use `Mockoon` to create our server. Mockoon is a set of free and open-source API mocking tools. (https://mockoon.com/)
The configuration of the server is all defined on the `data.json` file. (feel free to update the endpoints)

## (Option 1) 1. Expose local server via Cloudflare Tunnel

### 1.1 Create a Cloudflare Tunnel
- 1. Log into the dashboard (Zero Trust section)
- 2. Click on Access, then Tunnels
- 3. `Create Tunnel`, give it a name: `api-gateway` and Save
- 4. Select `Docker` from the available connectors and take note of the Token 

### 1.2 Run the local container
Add your token on `docker-compose.yml` (line 23) and run the docker containers (make sure Docker Desktop is launched)
```
# Run the container and test the following endpoints: http://localhost:3000/posts & http://localhost:3000/products
$ docker-compose up -d
```

### 1.3 Link to a public hostname
- 1. Return to the dashboard (your tunnel should be connecting to Cloudflare's edge.)
- 2. Configure your Tunnel
- 3. Click on `Public hostnames` then `add public hostname`
- 4. Provide the following infos:
    - Subdomain: `api`
    - Domain: Select one of your registered cloudflare domain
    - Type: `http`
    - URL: `api:3000`
- 5. Now your server is publicly accessible via `https://api.YOUR_DOMAIN`

Note: You will need to start and stop your Docker compose stack everytime you want to test your APIs

## (Option 2) 2. Deploy on GCP
### 2.1 Create the API server container
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

### 2.2 Deploy the image 
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

### 2.3 Create a Cloud Run service to publicly expose the API server
```
gcloud run deploy mockoon-image	\
 --image us-west2-docker.pkg.dev/PROJECT_ID/mockoon-docker-repo/mockoon-image:latest \
 --port='3000' \
 --allow-unauthenticated
```
Wait for the deployment to finish. Upon successful completion, a success message is displayed along with the `URL` of the deployed service.


### 2.4 Create CNAME record to proxy your traffic from Cloudflare
- 1. Log into the dashboard 
- 2. Go to your zone (e.g `example.com`) and click on `DNS`
- 3. `Add record`: Type -> `CNAME` , Name: `my-api` and Target: `YOUR_CLOUD_RUN_URL` (remove the https)
- 4. Click on `Rules` (left panel) and then `Origin Rules`
- 5. `Create rule` 
    - expression: `(http.host eq "my-api.YOUR_DOMAIN")`
    - rewrite to: `YOUR_CLOUD_RUN_URL` (remove the https)
    - Deploy
- 6. Now your server is publicly accessible via `https://my-api.YOUR_DOMAIN`


## 3. Generate API traffic on your zone

### 3.1 Bypass your traffic generator requests
By default Cloudflare will block requests coming from your traffic generator as they are considered as bot traffic. That can be avoided by creating a custom WAF rule to skip those rules. 
- 1. Log into the dashboard 
- 2. Go to your zone (e.g `example.com`) and click on `Security` (left panel)
- 4. Click on `WAF`  and then `Create rule` 
    - expression: `(http.host eq "api.YOUR_DOMAIN" and ip.src eq GENERATOR_IP)`
    - action: `Skip`
    - WAF components to skip: tick all the boxes
    - Deploy

### 3.2 Traffic generation
We will use Apache benchmark as traffic generator (https://httpd.apache.org/docs/2.4/programs/ab.html)
```
# Launch #10000 GET requests on an endpoint
$ $ ab -n 10000 https://api.YOUR_DOMAIN/endpoint1

# Launch #10000 POST requests on an endpoint
$ ab -n 10000  -p post_data.txt -T "application/json" https://api.YOUR_DOMAIN/endpoint2
```

Note: You will need wait between 12 to 48 hours to see your API traffic discoverable from the Cloudflare Dashboard (API GATEWAY)