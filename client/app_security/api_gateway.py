import requests
import os
import json


class APIGateway:

    def __init__(self, **kwargs):
        self.url = "https://api.cloudflare.com/client/v4"
        self.headers = {
            "Content-Type": "application/json", 
            "X-Auth-Email": os.environ.get("CF_EMAIL"),
            "X-Auth-Key": os.environ.get("CF_API_KEY")
        }
    
    #############  
    #############    GET METHODS   ###############
    #############
        



    #############    
    #############   POST METHODS   ###############
    ############# 
            
   


    #############    
    #############   DELETE METHODS   ###############
    ############# 
            