from django.urls import path
from . import views

urlpatterns = [
    path('', views.version_check, name='version-check'),  # Этот адрес будет использоваться приложением
    path('pro/', views.version_check_for_PRO, name='version-check-pro')
]