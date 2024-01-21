import json
from client.cf_client import Client


# DNS example
dns = Client(scope="dns").get()

ZONES = [ ("domain1.com", "full"), ("domain2.com", "full") ]
dns.create_multiple_zones(account_id="YOUR_ACCOUNT_ID", zones=ZONES)
dns.create_dns_record(zone_name="domain1.com", type="A", content="76.76.21.21", name="domain1.com") 


# Load Balancer example
lb = Client(scope="load_balancer").get()

lb.list_load_balancers(zone_name="YOUR_DOMAIN")