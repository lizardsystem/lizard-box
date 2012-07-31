lizard-box
==========================================

Introduction
------------

A box is a piece of content and can be displayed in full screen (Box
view), or as part of a Layout (Layout view).

Layouts can be defined using columns, and in it there are boxes.

Effectively you can configure all layouts in the django admin and then
go for it.

If you want a page in your root, you can configure something like this
in the urls.py::


    from lizard_box.views import BoxView
    ...

    url(r'^$',
        BoxView.as_view(),
        kwargs={'slug': 'home'},
        name='homepage'),

