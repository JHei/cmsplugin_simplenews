# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse_lazy
from .models import News

class LatestEntriesFeed(Feed):
    title = "Latest news"
    link = reverse_lazy('news_rss')
    description = "News RSS"

    def items(self):
        return News.published.all()[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
