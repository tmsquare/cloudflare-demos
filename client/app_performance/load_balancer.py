import requests
import os
import json


class LoadBalancer:
    ''' 
    #############    GET FUNCTIONS   ###############
    list_load_balancers(zone_name="example.com")

    #############    POST FUNCTIONS   ###############
    create_monitor(data=monitor_data) - monitor_data: dict
    create_pool(data=pool_data) - pool_data: dict
    create_load_balancer(data=lb_data) - lb_data: dict
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
            
    def create_monitor(self, **kwargs):

        data = kwargs.get('data')    
        req_data = {
            "expected_codes" : data['expected_codes'], 
            "description"    : data['description'],
            "type"           : data['type'],
            "port"           : data['port'],
            "interval"       : data['interval'],
            "timeout"        : data['timeout'],
            "retries"        : data['retries'],
        }
        print(self.headers)
        response = requests.post(f"{self.url}/user/load_balancers/monitors", headers=self.headers, json=req_data)
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=2))
            return (response.json())
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            
    def create_pool(self, **kwargs):

        data = kwargs.get('data')    
        req_data = {
            "name"           : data['name'], 
            "description"    : data['description'],
            "origins"        : data['origins'],
            "origin_steering": data['origin_steering'],
            "monitor"        : data['monitor'],
            "check_regions"  : data['check_regions']
        }
        
        response = requests.post(f"{self.url}/user/load_balancers/pools", headers=self.headers, json=req_data)
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=2))
            return (response.json())
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    def create_load_balancer(self, **kwargs):

        data = kwargs.get('data')    
        req_data = {
            "name"           : data['name'],
            "description"    : data['description'],
            "default_pools"  : data['default_pools'], 
            "fallback_pool"  : data['fallback_pool'],
            "steering_policy": data['steering_policy'],
        }
        zone_id = self.get_zone_id_by_name(zone_name=kwargs.get('zone_name'))['result'][0]["id"]
        response = requests.post(f"{self.url}/zones/{zone_id}/load_balancers", headers=self.headers, json=req_data)
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=2))
            return (response.json())
        else:
            print(f"Error: {response.status_code}")
            print(response.text)


    def create_pool(self):
        pass


    #############    
    #############   DELETE METHODS   ###############
    ############# 
            
    def delete_pool(self):
        pass