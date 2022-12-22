from ipware import get_client_ip
from .models import IPdata



class IPIsValid:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip, is_routable = get_client_ip(request)
        IPdata(ip=ip).save()


        response = self.get_response(request)
        return response




