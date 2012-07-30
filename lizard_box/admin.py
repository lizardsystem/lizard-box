# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from __future__ import unicode_literals

from django.contrib import admin

from lizard_box import models


class ColumnInline(admin.TabularInline):
    model = models.Column


class ColumnBoxInline(admin.TabularInline):
    model = models.ColumnBox


class LayoutAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        ColumnInline,
        ]


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('layout', 'index', )
    inlines = [
        ColumnBoxInline,
        ]


admin.site.register(models.Layout, LayoutAdmin)
admin.site.register(models.Column, ColumnAdmin)
admin.site.register(models.Box)

