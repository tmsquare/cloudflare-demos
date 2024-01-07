from load_balancer import LoadBalancer

ZONE_ID = "cd9491f4ae30cca95225d4000469427e"
EMAIL   = "mouhamadoutidiane@cloudflare.com"

lb = LoadBalancer(zone_id=ZONE_ID, email=EMAIL)

#lb.list_load_balancers()
lb.list_monitors()

'''  
curl --request GET \
  --url https://api.cloudflare.com/client/v4/mouhamadoutidiane@cloudflare.com/load_balancers/monitors \
  --header 'Content-Type: application/json' \
  --header 'X-Auth-Email: mouhamadoutidiane@cloudflare.com' \
  --header 'X-Auth-Key: e8367c05bafc6a7ec72b1c2cb271e961c721f'
'''