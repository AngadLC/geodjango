var map = L.map("map").setView([28.213961796748148,83.69376182556154], 7);
  
var osm = L.tileLayer(
  "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
  {
    attribution:
      "&copy; <a href='https://openstreetmap.org/copyright'> Openstreet map</a> contributors",
  }
);

var darkLayer = L.tileLayer(
  "https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png",
  {
    maxZoom: 20,
    attribution:
      '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
  }
);

var watercolor = L.tileLayer(
  "https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.{ext}",
  {
    attribution:
      'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    subdomains: "abcd",
    minZoom: 1,
    maxZoom: 16,
    ext: "jpg",
  }
);

var baseLayers = {
  osm: osm,
  "dark map": darkLayer,
  "water color map": watercolor,
};

osm.addTo(map);

L.control.layers(baseLayers).addTo(map);

//click on map
map.on("click",function(event){
  console.log(event.latlng)
})  






//Geojson style function
function geojsonStyle(feature) {
return {
  fillColor: getColor(feature.properties.region),
  weight: 2,
  opacity: 1,
  color: "#5e380f",
  fillOpacity: 0.7,
};
}

//GetColor function
function getColor(region) {
if (region == 1) {
  return "#008080";
} else if (region == 2) {
  return "#badd99";
} else if (region == 3) {
  return "#dd99ba";
} else {
  return "#c69540";
}
}

$.getJSON("{% url 'nepaldata' %}", function (data) {
console.log(data);
L.geoJSON(data, {
  onEachFeature: function (feature, layer) {
    layer.bindPopup(
      `<h5>district name: ${feature.properties.dist_name}</h5>`
    );
  },
  style: geojsonStyle,
}).addTo(map);
});