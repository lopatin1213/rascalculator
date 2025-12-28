from django.urls import path
from . import views

urlpatterns = [

    path('', views.main_view, name='main'),
    path('download', views.download, name='download'),
    path('version/<int:pk>', views.version_info, name='version-info'),

]