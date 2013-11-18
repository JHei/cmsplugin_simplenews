from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from menus.base import Menu, NavigationNode, Modifier
from menus.menu_pool import menu_pool
from .settings import SIMPLENEWS_PLUGIN_MENU_INDEX


class NewsMenu(Menu):
    def get_nodes(self, request):
        nodes = []
        n = NavigationNode(_('News'), reverse_lazy('news_list'), 1, attr={'targetIndex': SIMPLENEWS_PLUGIN_MENU_INDEX})
        nodes.append(n)
        return nodes


menu_pool.register_menu(NewsMenu)


class FollowModifier(Modifier):
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        if not post_cut:
            return nodes

        appNodes = [node for node in nodes if 'targetIndex' in node.attr]
        cmsNodes = [node for node in nodes if not 'targetIndex' in node.attr]

        resultNodes = []

        appNodeIndex = 0
        cmsNodeIndex = 0
        for resultNodeIndex in range(len(nodes)):
            if appNodeIndex < len(appNodes) and appNodes[appNodeIndex].attr['targetIndex'] == resultNodeIndex:
                resultNodes.append(appNodes[appNodeIndex])
                appNodeIndex += 1
            elif cmsNodeIndex < len(cmsNodes):
                resultNodes.append(cmsNodes[cmsNodeIndex])
                cmsNodeIndex += 1
            else:
                raise Exception('Error merging app menu and cms menu items')

        return resultNodes


menu_pool.register_modifier(FollowModifier)