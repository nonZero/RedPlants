"use strict";

function initialize() {

    var mapOptions = {}

    var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

    var latlngbounds = new google.maps.LatLngBounds();

    $("#obs li").each(function() {
        console.log($(this).data('lat'), $(this).data('lon'));
        var latlng = new google.maps.LatLng($(this).data('lat'), $(this).data('lon'));
        latlngbounds.extend(latlng);
        var marker = new google.maps.Marker({
            position : latlng,
            map : map,
            title : $(this).text()
        });

    });
    map.setCenter(latlngbounds.getCenter());
    map.fitBounds(latlngbounds);

}

google.maps.event.addDomListener(window, 'load', initialize); 