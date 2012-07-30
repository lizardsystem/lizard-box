# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from __future__ import unicode_literals

from django.utils.translation import ugettext as _
# from django.core.urlresolvers import reverse
# from lizard_map.views import MapView
from lizard_ui.views import UiView

from lizard_box import models


class LayoutView(UiView):
    """Layout"""
    template_name = 'lizard_box/layout.html'
    page_title = _('Layout')

    @property
    def layout(self):
        return get_object_or_404(models.Layout, slug=self.kwargs['slug'])


# class Todo2View(MapView):
#     """Simple view with a map."""
#     template_name = 'lizard_box/todo2.html'
#     page_title = _('TODO 2 view')
