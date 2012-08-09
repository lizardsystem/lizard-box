(function() {
  var after_dom_update_busy, columnBoxRefresh, divideVerticalSpaceEqually, initBoxDialog, initColumnBoxRefresh, initLevee, initSelectAllNone, initTargetLink, javascriptReplace, postFilterMeasurements;

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
      return $(element).find('.vertical-item.box-contents iframe').height(verticalItemHeight - 40);
    });
  };

  initBoxDialog = function() {
    return $(".box-dialog").each(function(index, element) {
      var data_attr_init;
      data_attr_init = "map_link_initialized_" + $(this).attr("data-temp-id");
      if ($("body").data(data_attr_init)) {
        if (!$(this).hasClass("ui-dialog-content")) $(this).remove();
        return;
      }
      $(this).dialog({
        autoOpen: false,
        title: $(this).attr("data-title"),
        minHeight: 400,
        width: $(window).width() - 200,
        height: $(window).height() - 200
      });
      return $("body").data(data_attr_init, true);
    });
  };

  initTargetLink = function() {
    $(".target-link").die();
    return $(".target-link").live("click", function(event) {
      var source_group, source_url;
      event.preventDefault();
      source_url = $(this).attr('href');
      source_group = $(this).attr('data-group');
      $('.target-destination[data-group="' + source_group + '"]').attr('data-src', source_url);
      $('.target-destination[data-group="' + source_group + '"]').load(source_url, function() {
        return console.log("Loaded " + source_group);
      });
      return false;
    });
  };

  columnBoxRefresh = function(temp_id) {
    var f;
    f = function() {
      return $.get('./', function(data) {
        var new_contents;
        console.log("ColumnBox refreshed: " + temp_id);
        new_contents = $(data).find('.box[data-temp-id="' + temp_id + '"]"').html();
        $('.box[data-temp-id="' + temp_id + '"]').html(new_contents);
        return javascriptReplace($('.box[data-temp-id="' + temp_id + '"]'));
      });
    };
    return f;
  };

  initColumnBoxRefresh = function() {
    console.log("Columnbox refresh");
    return $(".box").each(function() {
      var refresh_millis, temp_id;
      refresh_millis = $(this).attr("data-refresh-millis");
      temp_id = $(this).attr("data-temp-id");
      if (refresh_millis > 0) {
        console.log('set interval on ' + temp_id + ' millis: ' + refresh_millis);
        return setInterval(columnBoxRefresh(temp_id), refresh_millis);
      }
    });
  };

  javascriptReplace = function($selector) {
    if ($selector !== void 0) {
      return $selector.find(".javascript-replace").each(function(index, element) {
        var url;
        url = $(this).attr("data-src");
        return $(this).load(url, function() {
          return console.log("loaded url " + url);
        });
      });
    } else {
      return $(".javascript-replace").each(function(index, element) {
        var url;
        url = $(this).attr("data-src");
        return $(this).load(url, function() {
          return console.log("loaded url " + url);
        });
      });
    }
  };

  postFilterMeasurements = function() {
    var data, form, url;
    form = $("#filter-measurements");
    url = form.attr("action");
    data = {};
    form.find("input").each(function(index, element) {
      var checked, name;
      name = $(element).attr("name");
      checked = $(element).is(":checked");
      data[name] = checked;
      return console.log(name, checked);
    });
    return $.post(url, data, function() {
      var $target;
      console.log("update");
      $target = $(".target-destination[data-group='profile']");
      url = $target.attr("data-src");
      return $target.load(url);
    });
  };

  initSelectAllNone = function() {
    $("a.select-all").live("click", function(event) {
      event.preventDefault();
      $(this).parents("ul").find('input[type="checkbox"]').attr("checked", true);
      postFilterMeasurements();
      return false;
    });
    return $("a.select-none").live("click", function(event) {
      event.preventDefault();
      $(this).parents("ul").find('input[type="checkbox"]').attr("checked", false);
      postFilterMeasurements();
      return false;
    });
  };

  initLevee = function() {
    $("#filter-measurements input").die();
    $("#filter-measurements input").live("change", postFilterMeasurements);
    $("#filter-tags input").die();
    return $("#filter-tags input").live("change", function() {
      var data, form, url;
      form = $(this).parents("form");
      url = form.attr("action");
      data = {};
      form.find("input").each(function(index, element) {
        var checked, name;
        name = $(element).attr("name");
        checked = $(element).is(":checked");
        data[name] = checked;
        return console.log(name, checked);
      });
      return $.post(url, data);
    });
  };

  after_dom_update_busy = false;

  $(function() {
    $(".evenly-spaced-vertical").height($(window).height() - $("header").height() - $("#footer").height());
    $(".vertical-item-fixed").each(function(index, elem) {
      return $(elem).height($(elem).attr('data-height'));
    });
    $("#main-container").on("DOMNodeInserted", function(event) {
      if (!after_dom_update_busy) {
        after_dom_update_busy = true;
        return setInterval(function() {
          console.log("DOM modified event");
          initBoxDialog();
          $(".accordion").accordion();
          initTargetLink();
          initLevee();
          return after_dom_update_busy = false;
        }, 500);
      }
    });
    $(".box-action").live("click", function(event) {
      var temp_id;
      event.preventDefault();
      temp_id = $(this).attr("data-temp-id");
      $("div.box-dialog[data-temp-id=\"" + temp_id + "\"] iframe").each(function(index, element) {
        var src;
        src = $(element).attr("src");
        return $(element).attr("src", src);
      });
      $("div.box-dialog[data-temp-id=\"" + temp_id + "\"]").dialog('open');
      return false;
    });
    divideVerticalSpaceEqually();
    javascriptReplace();
    initColumnBoxRefresh();
    reloadGraphs();
    initLevee();
    return initSelectAllNone();
  });

  $(window).resize(function() {
    $(".evenly-spaced-vertical").height($(window).height() - $("header").height() - $("#footer").height());
    return divideVerticalSpaceEqually();
  });

}).call(this);
