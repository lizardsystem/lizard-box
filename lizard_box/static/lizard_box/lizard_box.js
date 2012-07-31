(function() {
  var divideVerticalSpaceEqually;

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
      return $(element).find('.vertical-item').height(verticalItemHeight);
    });
  };

  $(function() {
    $(".evenly-spaced-vertical").height($(window).height() - $("header").height() - $("#footer").height());
    $(".vertical-item-fixed").each(function(index, elem) {
      return $(elem).height($(elem).attr('data-height'));
    });
    $(".box-dialog").dialog({
      autoOpen: false,
      title: $(this).attr("data-title"),
      width: 900,
      height: 600
    });
    $(".box-action").live("click", function() {
      var temp_id;
      temp_id = $(this).attr("data-temp-id");
      console.log(temp_id);
      return $("div.box-dialog[data-temp-id=\"" + temp_id + "\"]").dialog('open');
    });
    return divideVerticalSpaceEqually();
  });

}).call(this);
