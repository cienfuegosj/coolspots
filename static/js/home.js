$(document).ready(function() {
  $("#personal_new").on("click", function(event) {
    $("#add_personal_modal").modal({keyboard: true});
    var notes_quill = new Quill('#p_notes', {
      theme: 'snow'
    });
    var assumptions_quill = new Quill('#p_assumptions', {
      theme: 'snow'
    });
    var constraints_quill = new Quill('#p_constraints', {
      theme: 'snow'
    });
  });
});

$(document).ready(function() {
  $("#team_new").on("click", function(event) {
    $("#add_team_modal").modal({keyboard: true});
      var notes_quill = new Quill('#t_notes', {
        theme: 'snow'
      });
      var assumptions_quill = new Quill('#t_assumptions', {
        theme: 'snow'
      });
      var constraints_quill = new Quill('#t_constraints', {
        theme: 'snow'
      });
  });
});

$(function () {
  $('#due_date_calendar').datetimepicker({
    minDate: moment()
  });
});

$(document).ready(function() {
    $('.btn-expand-collapse').click(function(e) {
    $("#favorite_panel").show();
        $("#recent_panel").show();
        $("#poll_panel").show();
	    $('.navbar-primary').toggleClass('collapsed');
    });

    $('#restaurant_btn').click(function(e) {
        $("#favorite_panel").show();
        $("#recent_panel").show();
        $("#poll_panel").show();
        $('#favorite_lbl').text("Favorite Restaurants");
        $('#recent_lbl').text("Recent Restaurants");
        $("#poll_date_lbl").text("When do you want to eat?")
        $("#location_lbl").text("Where do you want to eat?")
    });

    $('#parks_btn').click(function(e) {
        $("#favorite_panel").show();
        $("#recent_panel").show();
        $("#poll_panel").show();
        $('#favorite_lbl').text("Favorite Parks");
        $('#recent_lbl').text("Recent Parks");
        $("#poll_date_lbl").text("When do you want to visit the park?")
        $("#location_lbl").text("Where do you want to visit the park?")
    });
    $('#hotels_btn').click(function(e) {
        $("#favorite_panel").show();
        $("#recent_panel").show();
        $("#poll_panel").show();
        $('#favorite_lbl').text("Favorite Hotels");
        $('#recent_lbl').text("Recent Hotels");
        $("#poll_date_lbl").text("When do you plan to stay?")
        $("#location_lbl").text("Where do you want to stay?")
    });
    $('#coffee_btn').click(function(e) {
        $("#favorite_panel").show();
        $("#recent_panel").show();
        $("#poll_panel").show();
        $('#favorite_lbl').text("Favorite Coffee Shops");
        $('#recent_lbl').text("Recent Coffee Shops");
        $("#poll_date_lbl").text("When do you want to drink coffee?")
        $("#location_lbl").text("Where do you want to drink coffee?")
    });
    $('#hot_spots_btn').click(function(e) {
        $("#favorite_panel").show();
        $("#recent_panel").show();
        $("#poll_panel").show();
        $("#favorite_panel").hide();
        $("#recent_panel").hide();
        $("#poll_panel").hide();
        $(".main-content").append("<div id='googleMap'></div>");
        var mapProp= {
        center:new google.maps.LatLng(51.508742,-0.120850),
        zoom:5,};
        var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
};

        //using jquery, create a panel that display google map (div tag)
    });
});
