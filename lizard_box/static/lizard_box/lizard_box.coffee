divideVerticalSpaceEqually = () ->
    """ For .evenly-spaced-vertical, divide the vertical space evenly between
    the .vertical-item elements.  Take note of the 4px border between
    them. Inspired by lizard-ui.
    Handy for forms underneath the graphs, boxes, ....
    """
    $(".evenly-spaced-vertical").each (index, element) ->
        mainContentHeight = $(element).innerHeight()
        numberOfItems = $(element).find('.vertical-item').length

        # you can have items that have fixed heights, they are excluded from the stretching
        excludedItemsHeight = 0
        $(element).find('.vertical-item-fixed').each (index, fixed_element) ->
            excludedItemsHeight += $(fixed_element).innerHeight()

        verticalItemHeight = Math.floor(
            ((mainContentHeight-excludedItemsHeight) / numberOfItems)) - 1
        $(element).find('.vertical-item').height(verticalItemHeight)

$ ->
    console.log("hoi")
    $(".evenly-spaced-vertical").height($(window).height() - $("header").height() - $("#footer").height())
    $(".vertical-item-fixed").each (index, elem) ->
        console.log($(elem))
        $(elem).height($(elem).attr('data-height'))
    divideVerticalSpaceEqually()
