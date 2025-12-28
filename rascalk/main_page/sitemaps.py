from .models import Review, Vote
from django.contrib.sitemaps import Sitemap
class ReviewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Review.objects.all()

    def lastmod(self, obj):
        return obj.modified_date

class VoteSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Vote.objects.all()

    def lastmod(self, obj):
        return obj.modified_date

from for_adm.models import AppRasCalck, UserPro, news

class AppRasCalckSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return AppRasCalck.objects.all()

    def lastmod(self, obj):
        return obj.modified_date

class UserProSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.3

    def items(self):
        return UserPro.objects.all()

    def lastmod(self, obj):
        return obj.modified_date
class newssitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return news.objects.all()

    def lastmod(self, obj):
        return obj.modified_date
