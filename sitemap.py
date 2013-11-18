from django.contrib.sitemaps import Sitemap
from .models import News

class NewsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.4

    def items(self):
        return News.published.all()

    def lastmod(self, news):
        return news.pub_date
