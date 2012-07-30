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

    Can be used to display a part of a screen, or part of an "action" popup in upper right corner of a columnbox.
    """
    BOX_TYPE_CHOICES = (
        (1, "template in box"),
        (2, "iframe"),)

    name = models.CharField(
        _('title'),
        max_length=80)
    icon_class = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        help_text="bootstrap iconnames used as action in upper right corner: http://twitter.github.com/bootstrap/base-css.html")
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
                return 'Empty box: fill template of box named "%s"' % self.name
        elif self.box_type == 2:
            return '<iframe src="%s" frameborder="0">IFrame contents</iframe>' % self.url


class ColumnBox(models.Model):
    """
    A box in a column.
    """
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
    # Upper right corner, actions can be info, maximize
    action_boxes = models.ManyToManyField("Box", related_name="action_boxes")

    # add box_parameters?
    def render_box(self):
        return self.box.render()

    def display_name(self):
        """Display this name in a view"""
        if self.name:
            return self.name
        else:
            return self.box.name

    def actions(self):
        """
        Standard actions show in a popup. However, special actions
        like maximize or minimize can be "grabbed" by name in
        javascript lizard_box.js. These special actions do not exist
        yet.
        """
        return self.action_boxes.all()
