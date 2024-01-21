
# Application Perf python SDK

Interact with Cloudflare's products and services via the Cloudflare API.
This project wraps Cloudflare `App Performance` APIs using python. You can include it in your native python apps to programmatically interact with your CF account.  


## Prerequisites

Using the Cloudflare API requires authentication so that Cloudflare knows who is making requests and what permissions you have. Create an API token to grant access to the API to perform actions.

To create an API token, from the Cloudflare dashboard, go to My Profile > API Tokens and select Create Token. For more information on how to create and troubleshoot API tokens, refer to API fundamentals(`https://developers.cloudflare.com/fundamentals/api/`).

Before starting, export your credentials to your local terminal:
```
export CF_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export CF_EMAIL="xxxxxx@cloudflare.com"
```

Now you can use the `main.py` file tocimport the modules and start testing. 