# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
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
    portal_tabs = models.ManyToManyField("PortalTab", through="LayoutPortalTab")

    def __unicode__(self):
        return self.title


class PortalTab(models.Model):
    """
    A portal tab to link to other pages.

    You can define them on each layout.
    """
    TAB_TYPE_LAYOUT = 1
    TAB_TYPE_LINK = 2

    TAB_TYPE_CHOICES = (
        (TAB_TYPE_LAYOUT, "another lizard-box Layout"),
        (TAB_TYPE_LINK, "generic link"))

    name = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    icon_class = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        help_text="bootstrap iconnames used as action in upper right corner: http://twitter.github.com/bootstrap/base-css.html")

    tab_type = models.IntegerField(
        choices=TAB_TYPE_CHOICES,
        default=TAB_TYPE_LAYOUT)
    destination_slug = models.SlugField(
        help_text="in case of 'another lizard-box Layout'",
        null=True, blank=True)
    destination_url = models.CharField(
        help_text="URL in case of generic link",
        max_length=200,
        null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        """
        Calc destination url. The url does not really represent this
        object. On the other side, it does.
        """
        if self.tab_type == self.TAB_TYPE_LAYOUT:
            return reverse(
                "lizard_box_layoutview",
                kwargs={"slug": self.destination_slug})
        else:
            return self.destination_url


class LayoutPortalTab(models.Model):
    """A portal tab in a layout"""
    layout = models.ForeignKey(Layout)
    portal_tab = models.ForeignKey(PortalTab)
    index = models.IntegerField(default=100)

    class Meta:
        ordering = ('index', )


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

    class Meta:
        ordering = ('layout', 'index', )

    def __unicode__(self):
        return u'%s %d' % (self.layout, self.index)


class Box(models.Model):
    """
    A content holding item.

    Can be used to display a part of a screen, or part of an "action" popup in upper right corner of a columnbox.
    """
    BOX_TYPE_TEMPLATE = 1
    BOX_TYPE_IFRAME = 2
    BOX_TYPE_JSLOAD = 3

    BOX_TYPE_CHOICES = (
        (1, "template in box"),
        (2, "iframe"),
        (3, "js load"),
        )

    name = models.CharField(
        _('title'),
        max_length=80)
    slug = models.SlugField(
        _('slug'),
        help_text=_("Used in the URL."))
    icon_class = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        help_text="bootstrap iconnames used as action in upper right corner: http://twitter.github.com/bootstrap/base-css.html")
    box_type = models.IntegerField(choices=BOX_TYPE_CHOICES, default=BOX_TYPE_TEMPLATE)
    template = models.TextField(
        null=True, blank=True,
        help_text="For box_type 'template in box', or as optional selector in js loader")
    url = models.TextField(
        null=True,
        blank=True,
        help_text=_("For box_type 'iframe', url for iframe or source url for js loader")
        )

    def __unicode__(self):
        return self.name

    def render(self):
        if self.box_type == self.BOX_TYPE_TEMPLATE:
            if self.template:
                return self.template
            else:
                return 'Empty box: fill template of box named "%s"' % self.name
        elif self.box_type == self.BOX_TYPE_IFRAME:
            return '<iframe src="%s" frameborder="0">IFrame contents</iframe>' % self.url
        elif self.box_type == self.BOX_TYPE_JSLOAD:
            data_src = self.url
            if self.template:
                data_src += ' ' + self.template
            return '<div class="javascript-replace" data-src="%s">Loading</div>' % (
                data_src)


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
    action_boxes = models.ManyToManyField(
        "Box", related_name="action_boxes", null=True, blank=True)
    maximize_action = models.BooleanField(default=False)
    refresh_millis = models.IntegerField(
        default=0,
        help_text="refresh this columnbox every xxx millis, 0 for no refreshment")

    class Meta:
        ordering = ('index', )

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
        Standard actions show in a popup. However, special actions can
        be "grabbed" by name in javascript lizard_box.js. These
        special actions do not exist yet.
        """
        result = list(self.action_boxes.all())
        if self.maximize_action:
            action_box = self.box
            action_box.icon_class = 'icon-plus-sign'
            result.insert(0, action_box)
        return result
