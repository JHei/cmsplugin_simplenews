from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_simplenews.models import LatestNewsPlugin, News


class CMSLatestNewsPlugin(CMSPluginBase):
    """
        Plugin class for the latest news
    """
    model = LatestNewsPlugin
    name = _('Latest news')
    render_template = "cmsplugin_simplenews/latest_news.html"

    def render(self, context, instance, placeholder):
        """
            Render the latest news
        """
        latest = News.published.all()[:instance.limit]
        context.update({
            'instance': instance,
            'latest': latest,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(CMSLatestNewsPlugin)
