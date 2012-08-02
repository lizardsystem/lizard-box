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
        $(element).find('.vertical-item .box-contents').height(verticalItemHeight - 30)
        $(element).find('.vertical-item.box-contents iframe').height(verticalItemHeight - 40)  # let outer scrollbar disappear

initBoxDialog = () ->
    $(".box-dialog").dialog({
      autoOpen: false,
      title: $(this).attr("data-title"),
      minHeight: 400,
      width: $(window).width() - 200,
      height: $(window).height() - 200})

# you define <a href="urlwithcontents" class="target-link" data-group="groupname">link</a>
# and <div class="target-destination" data-group="groupname"></div>
# The result is that a click will fetch the url contents and place them in the target-destination.
initTargetLink = () ->
    $(".target-link").die()
    $(".target-link").live("click", (event) ->
        event.preventDefault()
        source_url = $(this).attr('href')
        source_group = $(this).attr('data-group')
        $('.target-destination[data-group="' + source_group + '"]').load(source_url, () ->
             console.log("Loaded " + source_group)
        )
        return false
    )


columnBoxRefresh = (temp_id) ->
    f = () ->
        $('.box[data-temp-id="' + temp_id + '"]').load('./ .box[data-temp-id="' + temp_id + '"]"', () ->
            console.log("ColumnBox refreshed: " + temp_id)
        )
    return f


initColumnBoxRefresh = () ->
    console.log("Columnbox refresh")
    $(".box").each(() ->
        refresh_millis = $(this).attr("data-refresh-millis")
        temp_id = $(this).attr("data-temp-id")  # should give unique columnbox id
        if refresh_millis > 0
            console.log('set interval on ' + temp_id + ' millis: ' + refresh_millis)
            setInterval(columnBoxRefresh(temp_id), refresh_millis)
    )


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

    #  DOMNodeInserted, DOMSubtreeModified
    $("#main-container").on("DOMNodeInserted", (event) ->
      # every time the DOM changes, check for new boxes
      console.log("DOM modified event")
      initBoxDialog()
      $(".accordion").accordion()
      initTargetLink()
    )

    # Find the item by slug, because the dialog itself has moved/vanished.
    $(".box-action").live("click", (event) ->
        event.preventDefault()
        temp_id = $(this).attr("data-temp-id")
        # console.log(temp_id)
        $("div.box-dialog[data-temp-id=\""+temp_id+"\"]").dialog('open')
        return false;
    )

    # divide the spaces
    divideVerticalSpaceEqually()

    # load the javascript loader based boxes
    $(".javascript-replace").each((index, element) ->
      url = $(this).attr("data-src")
      $(this).load(url, () ->
        console.log("loaded url " + url)
      )
    )

    # Some boxes are configured to refresh itself.
    # Experimental: popups appear multiple times, box contents are placed on a div too deep
    # initColumnBoxRefresh()


$(window).resize( () ->
    # give the evenly-spaced-vertical container its full height
    $(".evenly-spaced-vertical").height($(window).height() - $("header").height() - $("#footer").height())

      # divide the spaces
    divideVerticalSpaceEqually()

    #initBoxDialog()

    # Does not work well: the image maps themselves remain the same.
    # $(".javascript-replace .box").each(() ->
    #   height = $(this).innerHeight()
    #   #width = $(this).width()
    #   $(this).find("img").height(height)
    #   #$(this).find("img").width(width)
    #   )

    #$(".accordion").accordion()

    )

