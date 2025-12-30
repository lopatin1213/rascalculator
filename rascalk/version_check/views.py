

# Create your views here.
from django.http import HttpResponse

def version_check(request):
    # Версия вашего калькулятора
    VERSION = "9.20.43.20"
    return HttpResponse(VERSION)
def version_check_for_PRO(request):
    # Версия вашего калькулятора
    VERSION = "7.17.21.12"
    return HttpResponse(VERSION)
