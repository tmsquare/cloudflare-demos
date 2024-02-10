import json
from client.cf_client import Client

  
# DNS example
from client.cf_client import Client

ZONES = [("YOUR_DOMAIN", "full")]

# Create a zone 
dns = Client(scope="dns").get()
dns.create_multiple_zones(account_id="YOUR_ACCOUNT_ID", zones=ZONES)

# Add an A record
dns.create_dns_record(zone_name="YOUR_DOMAIN", type="A", content="76.76.21.21", name="YOUR_DOMAIN") 
