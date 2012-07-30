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
    BOX_TYPE_CHOICES = (
        (1, "template in box"),
        (2, "iframe"),)

    name = models.CharField(
        _('title'),
        max_length=80)
    box_type = models.IntegerField(choices=BOX_TYPE_CHOICES, default=1)
    template = models.TextField(
        null=True, blank=True,
        help_text="For box_type 'template in box'")
    url = models.URLField(
        null=True,
        blank=True,
        help_text=_("For box_type 'iframe', url for iframe")
        )

    def __unicode__(self):
        return self.name

    def render(self):
        if self.box_type == 1:
            if self.template:
                return self.template
            else:
                return 'Fill template of box named "%s"' % self.name
        elif self.box_type == 2:
            return '<iframe src="%s" frameborder="0">IFrame contents</iframe>' % self.url


class ColumnBox(models.Model):
    name = models.CharField(max_length=80, null=True, blank=True)
    box = models.ForeignKey(Box)
    column = models.ForeignKey(Column)
    index = models.IntegerField(
        default=100,
        help_text=_("Determines order of columns"))
    height = models.IntegerField(
        null=True,
        blank=True,
        help_text=_("Height in pixels, stretch if omitted"))

    # add box_parameters?
    def render_box(self):
        return self.box.render()

    def display_name(self):
        if self.name:
            return self.name
        else:
            return self.box.name
