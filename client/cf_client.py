from client.app_performance.dns import DNS
from client.app_performance.load_balancer import LoadBalancer
from client.app_security.api_gateway import APIGateway


class Client:
    ''' 
    #############    GET FUNCTIONS   ###############
    list_load_balancers(zone_name="example.com")
    '''

    def __init__(self, **kwargs):
        self.scope = kwargs.get('scope')
        self.get()


    def get(self):
        switch_dict = {
            'dns': DNS(),
            'load_balancer': LoadBalancer(),
            'api_gateway': APIGateway(),
        }

        # Use get() method to provide a default case
        return switch_dict.get(self.scope, DNS())
      
