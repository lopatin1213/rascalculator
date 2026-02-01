from django.http import HttpResponsePermanentRedirect
from django.conf import settings


class DomainRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        host = request.get_host()
        target_domain = getattr(settings, 'TARGET_DOMAIN', None)
        
        # Проверяем условие: если мы не находимся на localhost и задан целевой домен,
        # тогда выполняем перенаправление
        if not any(
                host.startswith(localhost) for localhost in ['localhost', '127.0.0.1']) and target_domain is not None:
            new_url = f'https://{target_domain}{request.path}'
            return HttpResponsePermanentRedirect(new_url)
        
        response = self.get_response(request)
        return response