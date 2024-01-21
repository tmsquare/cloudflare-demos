import requests
import os
import json


class LoadBalancer:

    def __init__(self, **kwargs):
        self.url = "https://api.cloudflare.com/client/v4"
        self.zone_id = kwargs.get('zone_id')
        self.headers = {
            "Content-Type": "application/json", 
            "X-Auth-Email": os.environ.get("CF_EMAIL"),
            "X-Auth-Key": os.environ.get("CF_API_KEY")
        }
    
    #############  
    #############    GET METHODS   ###############
    #############
        
    def list_load_balancers(self):
        response = requests.get(f"{self.url}/zones/{self.zone_id}/load_balancers", headers=self.headers)

        if response.status_code == 200:
            pretty_json = json.dumps(response.json(), indent=2)
            print(pretty_json)
        else:
            print(f"Error: {response.status_code}")
            print(response.text)



    #############    
    #############   POST METHODS   ###############
    ############# 
            
    def create_pool(self):
        pass


    #############    
    #############   DELETE METHODS   ###############
    ############# 
            
    def delete_pool(self):
        pass