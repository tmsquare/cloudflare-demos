import requests
import os
import json


class DNS:
    '''
    #############    GET FUNCTIONS   ###############
    list_dns_records(zone_name="example.com")
    list_zones(account_id="xxxxxxxx")
    get_analytics_report(zone_name="example.com")
    get_dnssec_details(zone_name="example.com")
    get_dns_record_details(zone_name="example.com", record_id="xxxxxxx")
    get_zone_details_by_name(zone_name="example.com")
    export_dns_records(zone_name="example.com")


    #############    POST FUNCTIONS   ###############
    edit_dnssec_details(zone_name="example.com", status="active")
    create_dns_record(zone_name="example.com", type="A", content="76.76.21.21", name="test.com")
    create_zone(account_id="xxxxxxx", name="example.com", type="partial")
    import_dns_records(zone_name="example.com", file="../../assets/file.txt")
    create_multiple_zones(account_id="xxxxxx", zones=ZONES)


    #############    DELETE FUNCTIONS   ###############
    delete_zone(zone_id="xxxxxxx")
    delete_dns_record(zone_name="example.com", record_id="xxxxxxx")
    delete_multiple_zones(zones=ZONES)


    #############    UPDATE FUNCTIONS   ###############
    update_dns_record(zone_name="example.com", record_id="xxxxxxx", type="CNAME", content="test.com", name="api.example.com")
    '''
    
    def __init__(self, **kwargs):
        self.url = "https://api.cloudflare.com/client/v4"
        
        self.headers = {
            "Content-Type": "application/json", 
            "X-Auth-Email": os.environ.get("CF_EMAIL") ,
            "X-Auth-Key": os.environ.get("CF_API_KEY") 
        }

        
    #############    GET FUNCTIONS   ###############
    def list_dns_records(self, **kwargs):
        zone_id = self.get_zone_details_by_name(zone_name=kwargs.get('zone_name'))['result'][0]["id"]
        response = requests.get(f"{self.url}/zones/{zone_id}/dns_records", headers=self.headers)

        if response.status_code == 200:
            return (response.json())            
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    def get_analytics_report(self, **kwargs):
        zone_id = self.get_zone_details_by_name(zone_name=kwargs.get('zone_name'))['result'][0]["id"]
        response = requests.get(f"{self.url}/zones/{zone_id}/dns_analytics/report", headers=self.headers)

        if response.status_code == 200:
            return (response.json())
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    def get_analytics_report_bytime(self, **kwargs):
        zone_id = self.get_zone_details_by_name(zone_name=kwargs.get('zone_name'))['result'][0]["id"]
        response = requests.get(f"{self.url}/zones/{zone_id}/dns_analytics/report/bytime", headers=self.headers)

        if response.status_code == 200:
            return (response.json())
        else:
            print(f"Error: {response.status_code}")
            print(response.text)


    def get_dnssec_details(self, **kwargs):
        zone_id = self.get_zone_details_by_name(zone_name=kwargs.get('zone_name'))['result'][0]["id"]
        response = requests.get(f"{self.url}/zones/{zone_id}/dnssec", headers=self.headers)

        if response.status_code == 200:
            return (response.json())
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    def export_dns_records(self, **kwargs):
        zone_id = self.get_zone_details_by_name(zone_name=kwargs.get('zone_name'))['result'][0]["id"]
        response = requests.get(f"{self.url}/zones/{zone_id}/dns_records/export", headers=self.headers)

        if response.status_code == 200:
            with open('dns_records.txt', 'w') as file:
                file.write(response.text)
            print(f"Succesully export on 'dns_records.txt'")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
    
    def get_dns_record_details(self, **kwargs):
        zone_id = self.get_zone_details_by_name(zone_name=kwargs.get('zone_name'))['result'][0]["id"]
        response = requests.get(f"{self.url}/zones/{zone_id}/dns_records/{kwargs.get('record_id')}", headers=self.headers)

        if response.status_code == 200:
            return (response.json())
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    
    def list_zones(self, **kwargs):
        response = requests.get(f"{self.url}/zones?account.id={kwargs.get('account_id')}", headers=self.headers)

        if response.status_code == 200:
            return (response.json())
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    def get_zone_details_by_name(self, **kwargs):
        response = requests.get(f"{self.url}/zones?name={kwargs.get('zone_name')}", headers=self.headers)

        if response.status_code == 200:
            return (response.json())
        else:
            print(f"Error: {response.status_code}")
            print(response.text)


 
    #############    PUT FUNCTIONS   ###############
    def update_dns_record(self, **kwargs):
        
        req_data = {
            "content": kwargs.get('content'), 
            "name"   : kwargs.get('name'),
            "type"   : kwargs.get('type'),
            "proxied": kwargs.get('proxied', True)
        }
        
        zone_id = self.get_zone_details_by_name(zone_name=kwargs.get('zone_name'))['result'][0]["id"]
        response = requests.put(f"{self.url}/zones/{zone_id}/dns_records/{kwargs.get('record_id')}", headers=self.headers, json=req_data)
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=2))
            return (response.json())
        else:
            print(f"Error: {response.status_code}")
            print(response.text)



    #############    POST FUNCTIONS   ###############
    def create_dns_record(self, **kwargs):
        
        req_data = {
            "content": kwargs.get('content'), 
            "name"   : kwargs.get('name'),
            "type"   : kwargs.get('type'),
            "proxied": kwargs.get('proxied', True)
        }
        
        zone_id = self.get_zone_details_by_name(zone_name=kwargs.get('zone_name'))['result'][0]["id"]
        response = requests.post(f"{self.url}/zones/{zone_id}/dns_records", headers=self.headers, json=req_data)
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=2))
            return (response.json())
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    def import_dns_records(self, **kwargs):
        
        self.headers["Content-Type"] = "multipart/form-data"
        with open(kwargs.get('file'), 'rb') as file:
            files = {'file': file}
            zone_id = self.get_zone_details_by_name(zone_name=kwargs.get('zone_name'))['result'][0]["id"]
            response = requests.post(f"{self.url}/zones/{zone_id}/dns_records/import", headers=self.headers, files=files)
        
        if response.status_code == 200:
            print("Records successfully updated")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)


    def create_zone(self, **kwargs):
        
        req_data = {
            "account": {
                 "id": kwargs.get('account_id')
                },
            "name"   : kwargs.get('name'),
            "type"   : kwargs.get('type', "full")
        }
        
        response = requests.post(f"{self.url}/zones", headers=self.headers, json=req_data)
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=2))
            return (response.json())
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    
    def create_multiple_zones(self, **kwargs):
        
        req_data = {
            "account": {
                 "id": kwargs.get('account_id')
                },
            "name"   : "",
            "type"   : ""
        }

        zones = kwargs.get('zones')
        for zone in zones:
            req_data["name"] = zone[0]
            req_data["type"] = zone[1]

            response = requests.post(f"{self.url}/zones", headers=self.headers, json=req_data)
            if response.status_code == 200:
                if zone[1] == "full":
                    name_servers = response.json()['result']['name_servers']
                    with open('zones_output.txt', 'a') as output_file:
                        output_file.write(f"Zone Name: {zone}\nName Servers: {', '.join(name_servers)}\n\n")
                else:
                    txt_record_name    = f"cloudflare-verify.{zone[0]}"
                    txt_record_content = response.json()['result']['verification_key']
                    with open('zones_output.txt', 'a') as output_file:
                        output_file.write(f"Zone Name: {zone}\nVerification TXT Record: {txt_record_name} {txt_record_content}\n\n")
                
            else:
                print(f"Error: {response.status_code}")
                print(response.text)
        
        print("Information written to 'zones_output.txt'")


    
    #############   DELETE FUNCTIONS   ###############
    def delete_dns_record(self, **kwargs):
        
        zone_id = self.get_zone_details_by_name(zone_name=kwargs.get('zone_name'))['result'][0]["id"]
        response = requests.delete(f"{self.url}/zones/{zone_id}/dns_records/{kwargs.get('record_id')}", headers=self.headers)
        if response.status_code == 200:
            print("Successfully deleted")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    def delete_zone(self, **kwargs):
        
        response = requests.delete(f"{self.url}/zones/{kwargs.get('zone_id')}", headers=self.headers)
        if response.status_code == 200:
            print("Successfully deleted")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)


    def delete_multiple_zones(self, **kwargs):
        
        zones = kwargs.get('zones')
        for zone in zones:
            zone_id = self.get_zone_details_by_name(zone_name=zone[0])['result'][0]["id"]
            response = requests.delete(f"{self.url}/zones/{zone_id}", headers=self.headers)
            if response.status_code == 200:
                print(f"{zone} successfully deleted")
            else:
                print(f"Error: {response.status_code}")
                print(response.text)


    #############  
    #############    PATCH METHODS   ###############
    #############
            
    def edit_dnssec_details(self, **kwargs):
        
        req_data = {
            "dnssec_multi_signer": kwargs.get('multi_signer', False), 
            "dnssec_presigned"   : kwargs.get('presigned', True),
            "status"             : kwargs.get('status', "disabled") 
        }
        
        zone_id = self.get_zone_details_by_name(zone_name=kwargs.get('zone_name'))['result'][0]["id"]
        response = requests.put(f"{self.url}/zones/{zone_id}/dnssec", headers=self.headers, json=req_data)
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=2))
            
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
