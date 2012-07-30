# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Layout(models.Model):
    """
    A layout consists of one of more columns with contents (boxes).
    """
    title = models.CharField(
        _('title'),
        max_length=80)
    slug = models.SlugField(
        _('slug'),
        help_text=_("Used in the URL."))

    def __unicode__(self):
        return self.title


class Column(models.Model):
    """
    A part of Layout, containing Boxes.
    """
    layout = models.ForeignKey(Layout)
    width = models.IntegerField(
        null=True,
        blank=True,
        help_text=_("Width 1-12 following Twitter Bootstrap scaffolding"))
    index = models.IntegerField(
        default=100,
        help_text=_("Determines order of columns"))
    boxes = models.ManyToManyField("Box", through="ColumnBox")

    def __unicode__(self):
        return u'%s %d' % (self.layout, self.index)


class Box(models.Model):
    """
    A content holding item.
    """
    name = models.CharField(
        _('title'),
        max_length=80)

    def __unicode__(self):
        return self.name


class ColumnBox(models.Model):
    box = models.ForeignKey(Box)
    column = models.ForeignKey(Column)
    index = models.IntegerField(
        default=100,
        help_text=_("Determines order of columns"))


