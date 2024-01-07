from load_balancer import LoadBalancer

ZONE_ID = "cxxxxxxxxxxxxxxxxe"
EMAIL   = "xxxxxxxxxxx@cloudflare.com"

lb = LoadBalancer(zone_id=ZONE_ID, email=EMAIL)

#lb.list_load_balancers()
lb.list_monitors()
