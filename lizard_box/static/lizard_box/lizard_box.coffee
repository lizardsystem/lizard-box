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
    $(".box-dialog").each((index, element) ->
      # Special measurements because the page can be dynamic. New
      # instances can appear for each data-temp-id, but we want to
      # ignore those. Note that more and more of the same box-dialog
      # objects appear during a session.
      data_attr_init = "map_link_initialized_" + $(this).attr("data-temp-id")
      if $("body").data(data_attr_init)  # the popup exists
        if not $(this).hasClass("ui-dialog-content")  # and the popup is not this object
          $(this).remove()
        return
      $(this).dialog({
        autoOpen: false,
        title: $(this).attr("data-title"),
        minHeight: 400,
        width: 960,
        height: 500})
      $("body").data(data_attr_init, true)
    )

# you define <a href="urlwithcontents" class="target-link" data-group="groupname">link</a>
# and <div class="target-destination" data-group="groupname"></div>
# The result is that a click will fetch the url contents and place them in the target-destination.
initTargetLink = () ->
    $(".target-link").die()
    $(".target-link").live("click", (event) ->
        event.preventDefault()
        source_url = $(this).attr('href')
        source_group = $(this).attr('data-group')
        # place the link in it for future reference
        $('.target-destination[data-group="' + source_group + '"]').attr('data-src', source_url);
        $('.target-destination[data-group="' + source_group + '"]').load(source_url, () ->
             console.log("Loaded " + source_group)
        )
        return false
    )


columnBoxRefresh = (temp_id) ->
    f = () ->
        # refresh single element
        # $('.box[data-temp-id="' + temp_id + '"]').load('./ .box[data-temp-id="' + temp_id + '"]"', () ->
        #     console.log("ColumnBox refreshed: " + temp_id)
        # )
        $.get('./', (data) ->
            console.log("ColumnBox refreshed: " + temp_id)
            new_contents = $(data).find('.box[data-temp-id="' + temp_id + '"]"').html()
            $('.box[data-temp-id="' + temp_id + '"]').html(new_contents)
            javascriptReplace($('.box[data-temp-id="' + temp_id + '"]'))
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

javascriptReplace = ($selector) ->
    if $selector != undefined
      $selector.find(".javascript-replace").each((index, element) ->
        url = $(this).attr("data-src")
        $(this).load(url, () ->
          console.log("loaded url " + url)
        )
      )
    else
      $(".javascript-replace").each((index, element) ->
        url = $(this).attr("data-src")
        $(this).load(url, () ->
          console.log("loaded url " + url)
        )
      )


# Levee specific
#
#
postFilterMeasurements = () ->
    form = $("#filter-measurements")
    url = form.attr("action")
    data = {}
    form.find("input").each((index, element) ->
      name = $(element).attr("name")
      checked = $(element).is(":checked")
      data[name] = checked
      # Strange: if you remove the console.log, the input objects do not all appear in the output
      console.log(name, checked)
    )
    #console.log(data)
    $.post(url, data, () ->
      console.log("update")
      # We know that data-slug "profiel" has js-loaded contents in <div class="javascript-replace">, reload it.
      $target = $(".target-destination[data-group='profile']")
      url = $target.attr("data-src")
      $target.load(url)
    )

initSelectAllNone = () ->
  $("a.select-all").live("click", (event) ->
    event.preventDefault()
    $(this).parents("ul").find('input[type="checkbox"]').attr("checked", true)
    postFilterMeasurements()
    return false
  )
  $("a.select-none").live("click", (event) ->
    event.preventDefault()
    $(this).parents("ul").find('input[type="checkbox"]').attr("checked", false)
    postFilterMeasurements()
    return false
  )

initLevee = () ->
  $("#filter-measurements input").die()
  $("#filter-measurements input").live("change", postFilterMeasurements)
  # $("#filter-tags a").live("click", (event) ->
  #   event.preventDefault()
  #   return false
  #   )
  $("#filter-tags input").die()
  $("#filter-tags input").live("change", () ->
    form = $(this).parents("form")
    url = form.attr("action")
    data = {}
    form.find("input").each((index, element) ->
      name = $(element).attr("name")
      checked = $(element).is(":checked")
      data[name] = checked
      # Strange: if you remove the console.log, the input objects do not all appear in the output
      console.log(name, checked)
    )
    $.post(url, data)
  )

  # Graphs
  $("a.select-point-set").die()
  $("a.select-point-set").live("click", () ->
    form = $(this).parents("form")
    url = form.attr("action")
    data = {point_set: $(this).attr("data-point-set-id")}

    $(this).addClass("point-set-selected")  # make it feel snappier

    $.post(url, data, (data) ->
      $("#point-set-selection").html($(data).find("#point-set-selection").html())
      $("#point-set-graph-selection").html($(data).find("#point-set-graph-selection").html())
      $("#point-set-graphs").html($(data).find("#point-set-graphs").html())
    )
  )

  $("input.select-point").die()
  $("input.select-point").live("change", () ->
    form = $(this).parents("form")
    url = form.attr("action")
    data = {
      point_from_point_set: $(this).attr("data-point-set-id"),
      point: $(this).attr("data-point-id"),
      point_checked: $(this).is(":checked")
    }

    $.post(url, data, (data) ->
      $("#point-set-graphs").html($(data).find("#point-set-graphs").html())
    )
  )
#
# End levee specific


# after_dom_update_busy = false

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

    #  DOMNodeInserted, DOMSubtreeModified: only after 500 ms
    $("#main-container").on("DOMNodeInserted", (event) ->
      # if not after_dom_update_busy
      #   after_dom_update_busy = true
      #   setInterval(() ->
          # every time the DOM changes, check for new boxes
          console.log("DOM modified event")
          initBoxDialog()
          $(".accordion").accordion()
          initTargetLink()
          initLevee()
          #reloadGraphs()  # from lizardui
        #   after_dom_update_busy = false
        # , 500)
    )

    # Find the item by slug, because the dialog itself has moved/vanished.
    $(".box-action").live("click", (event) ->
        event.preventDefault()
        temp_id = $(this).attr("data-temp-id")
        # reload iframe after clicking a box-action.
        $("div.box-dialog[data-temp-id=\""+temp_id+"\"] iframe").each((index, element) ->
          # Should be only one
          src = $(element).attr("src")
          $(element).attr("src", src)
        )
        # open target
        $("div.box-dialog[data-temp-id=\""+temp_id+"\"]").dialog('open')
        return false;
    )

    # divide the spaces
    divideVerticalSpaceEqually()

    # load the javascript loader based boxes
    javascriptReplace()

    # Some boxes are configured to refresh itself.
    # Experimental: popups appear multiple times, box contents are placed on a div too deep
    initColumnBoxRefresh()
    reloadGraphs()  # from lizardui

    initLevee()

    # "select-all" and "select-none"
    initSelectAllNone()


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

