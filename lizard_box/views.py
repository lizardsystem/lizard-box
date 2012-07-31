# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from __future__ import unicode_literals

from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404
# from django.core.urlresolvers import reverse
# from lizard_map.views import MapView
from lizard_ui.views import UiView
from lizard_ui.layout import Action

from lizard_box import models


class LayoutView(UiView):
    """Layout"""
    template_name = 'lizard_box/layout.html'
    #page_title = _('Layout')

    @property
    def page_title(self):
        return str(self.layout)

    @property
    def site_actions(self):
        actions = []
        for portal_tab in self.layout.portal_tabs.all():
            print portal_tab
            actions.append(
                Action(
                    name=portal_tab.name,
                    description=portal_tab.description,
                    url=portal_tab.get_absolute_url(),
                    icon=portal_tab.icon_class)
                )
        return actions + super(LayoutView, self).site_actions

    @property
    def layout(self):
        return get_object_or_404(models.Layout, slug=self.kwargs['slug'])


class BoxView(UiView):
    """Display a single box in full screen, with surrounding lizard-ui
    items.
    """

    template_name = 'lizard_box/box.html'
    #page_title = 'Box'  # apparently used for breadcrumbs

    @property
    def page_title(self):
        return str(self.box)

    @property
    def box(self):
        return get_object_or_404(models.Box, slug=self.kwargs['slug'])
