# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import NewsList, NewsDetail
from .feed import LatestEntriesFeed

urlpatterns = patterns('',
    url(r'^rss/$', LatestEntriesFeed(), name='news_rss'),
    url(r'^$', NewsList.as_view(), name='news_list'),
    url(r'^(?P<slug>[\w-]+)/$', NewsDetail.as_view(), name='news_detail'),
)
