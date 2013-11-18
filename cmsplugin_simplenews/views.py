# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from .models import News

class NewsList(ListView):
    template_name = 'cmsplugin_simplenews/news_list.html'
    queryset = News.published.all()
    context_object_name = 'news_list'
    paginate_by = 5

class NewsDetail(DetailView):
    template_name = 'cmsplugin_simplenews/news_detail.html'
    context_object_name = 'news'
    model = News
