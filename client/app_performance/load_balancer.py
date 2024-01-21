import requests
import os
import json


class LoadBalancer:
    ''' 
    #############    GET FUNCTIONS   ###############
    list_load_balancers(zone_name="example.com")
    '''

    def __init__(self, **kwargs):
        self.url = "https://api.cloudflare.com/client/v4"
        self.headers = {
            "Content-Type": "application/json", 
            "X-Auth-Email": os.environ.get("CF_EMAIL"),
            "X-Auth-Key": os.environ.get("CF_API_KEY")
        }
    
    def get_zone_id_by_name(self, **kwargs):
        response = requests.get(f"{self.url}/zones?name={kwargs.get('zone_name')}", headers=self.headers)

        if response.status_code == 200:
            return (response.json()['result'][0]["id"])
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
    
    #############  
    #############    GET METHODS   ###############
    #############
        
    def list_load_balancers(self, **kwargs):
        zone_id = self.get_zone_id_by_name(zone_name=kwargs.get('zone_name'))
        response = requests.get(f"{self.url}/zones/{zone_id}/load_balancers", headers=self.headers)

        if response.status_code == 200:
            pretty_json = json.dumps(response.json(), indent=2)
            print(pretty_json)
            return (response.json())
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