from django.urls import path
from . import views

urlpatterns = [

    path('', views.view, name='main-android'),
    path('download', views.download, name='download-android'),
    path('version/<int:pk>', views.version_info_android, name='version-info-android'),

]