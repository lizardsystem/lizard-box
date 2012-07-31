# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin
from lizard_ui.urls import debugmode_urlpatterns

from lizard_box import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    # url(r'^ui/', include('lizard_ui.urls')),
    # url(r'^map/', include('lizard_map.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^layout/(?P<slug>[^/]+)/',
        views.LayoutView.as_view(),
        name="lizard_box_layoutview"),
    url(r'^box/(?P<name>[^/]+)/',
        views.BoxView.as_view(),
        name="lizard_box_boxview"),
   # url(r'^something_else/$',
    #     views.SomeClassBasedView.as_view(),
    #     name='name_it_too'),
    )
urlpatterns += debugmode_urlpatterns()
