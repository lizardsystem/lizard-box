# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from __future__ import unicode_literals

from django.contrib import admin

from lizard_box import models


class ColumnInline(admin.TabularInline):
    model = models.Column


class LayoutPortalTabInline(admin.TabularInline):
    model = models.LayoutPortalTab


class ColumnBoxInline(admin.TabularInline):
    model = models.ColumnBox


class LayoutAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        ColumnInline, LayoutPortalTabInline,
        ]


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('layout', 'index', )
    inlines = [
        ColumnBoxInline,
        ]


class BoxAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}


admin.site.register(models.Layout, LayoutAdmin)
admin.site.register(models.Column, ColumnAdmin)
admin.site.register(models.Box, BoxAdmin)
admin.site.register(models.PortalTab)

