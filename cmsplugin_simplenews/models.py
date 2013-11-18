import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from cms.models import CMSPlugin
from tinymce.models import HTMLField


class PublishedNewsManager(models.Manager):
    """
        Filters out all unpublished and items with a publication date in the future
    """

    def get_query_set(self):
        return super(PublishedNewsManager, self).get_query_set() \
            .filter(is_published=True) \
            .filter(pub_date__lte=datetime.datetime.now())


class News(models.Model):
    """
    News
    """

    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(_('Slug'), unique_for_date='pub_date', max_length=50,
                            help_text=_('A slug is a short name which uniquely identifies the news item for this day'))
    content = HTMLField(_('Content'), blank=True)

    is_published = models.BooleanField(_('Published'), default=False)
    pub_date = models.DateTimeField(_('Publication date'), default=datetime.datetime.now())

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    published = PublishedNewsManager()
    objects = models.Manager()

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
        ordering = ('-pub_date', )

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.slug)])


class LatestNewsPlugin(CMSPlugin):
    """
        Model for the settings when using the latest news cms plugin
    """
    limit = models.PositiveIntegerField(_('Number of news items to show'), default=3,
                                        help_text=_('Limits the number of items that will be displayed'))
