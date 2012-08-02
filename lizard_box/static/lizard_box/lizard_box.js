(function() {
  var divideVerticalSpaceEqually, initBoxDialog, initTargetLink;

  divideVerticalSpaceEqually = function() {
    " For .evenly-spaced-vertical, divide the vertical space evenly between\nthe .vertical-item elements.  Take note of the 4px border between\nthem. Inspired by lizard-ui.\nHandy for forms underneath the graphs, boxes, ....";    return $(".evenly-spaced-vertical").each(function(index, element) {
      var excludedItemsHeight, mainContentHeight, numberOfItems, verticalItemHeight;
      mainContentHeight = $(element).innerHeight();
      numberOfItems = $(element).find('.vertical-item').length;
      excludedItemsHeight = 0;
      $(element).find('.vertical-item-fixed').each(function(index, fixed_element) {
        return excludedItemsHeight += $(fixed_element).innerHeight();
      });
      verticalItemHeight = Math.floor((mainContentHeight - excludedItemsHeight) / numberOfItems) - 1;
      $(element).find('.vertical-item').height(verticalItemHeight);
      $(element).find('.vertical-item .box-contents').height(verticalItemHeight - 30);
      return $(element).find('.vertical-item iframe').height(verticalItemHeight - 40);
    });
  };

  initBoxDialog = function() {
    return $(".box-dialog").dialog({
      autoOpen: false,
      title: $(this).attr("data-title"),
      minHeight: 400,
      width: $(window).width() - 200,
      height: $(window).height() - 200
    });
  };

  initTargetLink = function() {
    $(".target-link").die();
    return $(".target-link").live("click", function(event) {
      var source_group, source_url;
      event.preventDefault();
      source_url = $(this).attr('href');
      source_group = $(this).attr('data-group');
      $('.target-destination[data-group="' + source_group + '"]').load(source_url, function() {
        return console.log("Loaded " + source_group);
      });
      return false;
    });
  };

  $(function() {
    $(".evenly-spaced-vertical").height($(window).height() - $("header").height() - $("#footer").height());
    $(".vertical-item-fixed").each(function(index, elem) {
      return $(elem).height($(elem).attr('data-height'));
    });
    $("#main-container").on("DOMNodeInserted", function(event) {
      console.log("DOM modified event");
      initBoxDialog();
      $(".accordion").accordion();
      return initTargetLink();
    });
    $(".box-action").live("click", function(event) {
      var temp_id;
      event.preventDefault();
      temp_id = $(this).attr("data-temp-id");
      $("div.box-dialog[data-temp-id=\"" + temp_id + "\"]").dialog('open');
      return false;
    });
    divideVerticalSpaceEqually();
    return $(".javascript-replace").each(function(index, element) {
      var url;
      url = $(this).attr("data-src");
      return $(this).load(url, function() {
        return console.log("loaded url " + url);
      });
    });
  });

  $(window).resize(function() {
    $(".evenly-spaced-vertical").height($(window).height() - $("header").height() - $("#footer").height());
    return divideVerticalSpaceEqually();
  });

}).call(this);
