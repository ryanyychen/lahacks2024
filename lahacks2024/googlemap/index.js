let map;

// require('dotenv').config();

const API_KEY = "AIzaSyBk6mPEMyEkSzlwE11KmcCcS_DWBmMfg-0";

async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");

  map = new Map(document.getElementById("map"), {
    center: { lat: 40.712776, lng: -74.005974 },
    zoom: 8,
  });

  const image =
    "./person_pin.png";
  const marker = new google.maps.Marker({
    position: { lat: 40.712776, lng: -74.005974 }, // Marker position
    map: map, // Map to add the marker to
    icon: image,
  });
}

initMap();