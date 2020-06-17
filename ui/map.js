const width = 3000;
const height = 1500;

let projection = d3
    .geoEquirectangular()
    .center([0, 15])
    .scale([w/(2*Math.PI)])
    .translate([w/2, h/2]);

var path = d3.geoPath().projection(projection);

var svg = d3.select('#map').append('svg').attr('width', $('#map-holder').width()).attr('height', $('#map-holder').height())

function getTextBox(selection) {
    selection.each(function(d) {
        d.bbox = this.getBBox()
    });
}

// To look up:
// var vs let (vs const)
// Python generators
// arrow functions and other function declaration styles