"""
URL configuration for rascalk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from for_adm.views import check_user

from django.contrib.sitemaps.views import sitemap
from main_page.sitemaps import ReviewSitemap, VoteSitemap, AppRasCalckSitemap, UserProSitemap, newssitemap

sitemaps = {
    'main_pages': ReviewSitemap(),  # Карта сайта для основного приложения
    'admin_pages': VoteSitemap(),
    'apprascalck': AppRasCalckSitemap(),
    'pro': UserProSitemap(),
    'news': newssitemap()

}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls')),
    path('check_user/<str:username>/<str:secret_key>/', check_user, name='check_user'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('android/', include('android.urls'))
]




from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static('/', document_root=settings.BASE_DIR)
