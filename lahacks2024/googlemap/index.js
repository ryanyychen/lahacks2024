let map;

// require('dotenv').config();

const API_KEY = "AIzaSyBk6mPEMyEkSzlwE11KmcCcS_DWBmMfg-0";

const PASSENGER = "M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zm-45.7 48C79.8 304 0 383.8 0 482.3C0 498.7 13.3 512 29.7 512H418.3c16.4 0 29.7-13.3 29.7-29.7C448 383.8 368.2 304 269.7 304H178.3z";
const DRIVER = "M135.2 117.4L109.1 192H402.9l-26.1-74.6C372.3 104.6 360.2 96 346.6 96H165.4c-13.6 0-25.7 8.6-30.2 21.4zM39.6 196.8L74.8 96.3C88.3 57.8 124.6 32 165.4 32H346.6c40.8 0 77.1 25.8 90.6 64.3l35.2 100.5c23.2 9.6 39.6 32.5 39.6 59.2V400v48c0 17.7-14.3 32-32 32H448c-17.7 0-32-14.3-32-32V400H96v48c0 17.7-14.3 32-32 32H32c-17.7 0-32-14.3-32-32V400 256c0-26.7 16.4-49.6 39.6-59.2zM128 288a32 32 0 1 0 -64 0 32 32 0 1 0 64 0zm288 32a32 32 0 1 0 0-64 32 32 0 1 0 0 64z"

async function initMap(lat, lng) {
  const { Map } = await google.maps.importLibrary("maps");

  const map = new Map(document.getElementById("map"), {
    center: { lat: lat, lng: lng },
    zoom: 17,
  });
  
  add_object("TW", 34.0694773, -118.4466582, 'blue','passenger', map);
  add_object("RC", 34.0702679, -118.4457981, 'blue','driver', map);
  add_object("CD", 34.0594773, -118.4566582, 'red','driver', map);
  add_object("KV", 34.0708773, -118.4366582, 'red','passenger', map);
}

function add_object(name, lat, lng, color, type, map) {
  var svgMarker = {};
  if(type == "passenger") {
    svgMarker = {
      path: PASSENGER,
      fillColor: color,
      fillOpacity: 0.6,
      strokeWeight: 0,
      rotation: 0,
      scale: 0.05,
      // anchor: new google.maps.Point(0, 20),
    };
  }
  else {
    svgMarker = {
      path: DRIVER,
      fillColor: color,
      fillOpacity: 0.6,
      strokeWeight: 0,
      rotation: 0,
      scale: 0.05,
      // anchor: new google.maps.Point(0, 20),
    };
  }

  new google.maps.Marker({
    position: { lat: lat, lng: lng },
    icon: svgMarker,
    map: map,
    label: name,
  });
  // new google.maps.MarkerWithLabel({
  //   position: { lat: lat, lng: lng },
  //   icon: svgMarker,
  //   map: map,
  //   labelContent: name,
  // });
}

initMap(34.0694773, -118.4466582);