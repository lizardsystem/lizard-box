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
    # give the evenly-spaced-vertical container its full height
    $(".evenly-spaced-vertical").height($(window).height() - $("header").height() - $("#footer").height())

    # apply all fixed heights
    $(".vertical-item-fixed").each (index, elem) ->
        $(elem).height($(elem).attr('data-height'))

    # make .box-dialog show dialogs
    # $(".box-dialog").live("click", () ->
    #     $(this).dialog({title: $(this).attr("data-title")})
    #     )

    $(".box-dialog").dialog({
      autoOpen: false,
      title: $(this).attr("data-title"),
      width: 900,
      height: 600})
    # Find the item by slug, because the dialog itself has moved/vanished.
    $(".box-action").live("click", () ->
        temp_id = $(this).attr("data-temp-id")
        console.log(temp_id)
        $("div.box-dialog[data-temp-id=\""+temp_id+"\"]").dialog('open')

        #alert("hallo")
    )

    # divide the spaces
    divideVerticalSpaceEqually()
