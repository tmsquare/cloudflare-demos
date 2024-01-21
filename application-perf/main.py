import json
from modules.load_balancer import LoadBalancer
from modules.dns import DNS


ZONE_ID = "xxxxxxxxxxxxxxxxxxxxxx"
ZONES = [
    ("domain1.com", "full"),
    ("domain2.com", "full"),
]

lb = LoadBalancer(zone_id=ZONE_ID)
#lb.list_load_balancers()


dns = DNS(zone_id=ZONE_ID)
#data = dns.list_dns_records()
#data = dns.get_analytics_report()
#data = dns.get_dnssec_details()
#data = dns.edit_dnssec_details(status="active")
#data = dns.get_dns_record_details(id="xxxxxxx")
#data = dns.update_dns_record(id="xxxxxxx", type="CNAME", content="test.com", name="api.example.com")
#data = dns.create_dns_record(type="A", content="76.76.21.21", name="test.com")
#data = dns.list_zones(account_id="xxxxxxxx")
#data = dns.get_zone_details_by_name(zone_name="example.com")
#data = dns.get_zone_details_by_id()
#data = dns.create_zone(account_id="xxxxxxx", name="example.com", type="partial")
#dns.delete_zone(zone_id="xxxxxxx")
#dns.delete_dns_record(id="xxxxxxx")
#dns.export_dns_records()
#dns.import_dns_records(file="./assets/file.txt")
#dns.create_multiple_zones(account_id="xxxxxx", zones=ZONES)
#dns.delete_multiple_zones(zones=ZONES)

#print(json.dumps(data, indent=2))