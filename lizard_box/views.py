# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from __future__ import unicode_literals

# from django.core.urlresolvers import reverse
# from django.utils.translation import ugettext as _
# from lizard_map.views import MapView
from django.shortcuts import get_object_or_404
from lizard_ui.layout import Action
from lizard_ui.views import UiView

from lizard_box import models


class LayoutView(UiView):
    """Layout"""
    template_name = 'lizard_box/layout.html'
    #page_title = _('Layout')

    @property
    def page_title(self):
        return self.layout.title

    @property
    def edit_link(self):
        return '/admin/lizard_box/layout/{pk}/'.format(
            pk=self.layout.pk)

    @property
    def layout(self):
        return get_object_or_404(models.Layout, slug=self.kwargs['slug'])


class BoxView(UiView):
    """Display a single box in full screen, with surrounding lizard-ui
    items.
    """

    template_name = 'lizard_box/box.html'

    @property
    def edit_link(self):
        return '/admin/lizard_box/box/{pk}/'.format(
            pk=self.box.pk)

    @property
    def page_title(self):
        return str(self.box)

    @property
    def box(self):
        return get_object_or_404(models.Box, slug=self.kwargs['slug'])

    @property
    def breadcrumbs(self):
        """Return breadcrumbs (only if we're the homepage).

        If we have the 'home' slug, we're used as the homepage,
        apparently. Return specifically only the 'home' breadcrumb in that
        case. Otherwise return None so that the fallback kicks in.

        """
        if self.kwargs['slug'] == 'home':
            return [self.home_breadcrumb_element]
