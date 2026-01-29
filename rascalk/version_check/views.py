

# Create your views here.
from django.http import HttpResponse
from for_adm.models import AppRasCalck
def version_check(request):
    # Версия вашего калькулятора
    version = AppRasCalck.objects.filter(is_latest=True).first()
    VERSION = version.version
    
    return HttpResponse(VERSION)
def version_check_for_PRO(request):
    # Версия вашего калькулятора
    VERSION = "7.17.21.12"
    return HttpResponse(VERSION)
