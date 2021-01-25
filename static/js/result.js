// Load google charts
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

// Draw the chart and set the chart values
function drawChart() {
  var data = google.visualization.arrayToDataTable([
  ['Result','DAA'],
  ['Right Answer',65],
  ['Wrong Answer',40],
  ['Not Attempted',15],
]);

  // Optional; add a title and set the width and height of the chart
  var options = {
      title : "Result",
      is3D: true,
      width: 900,
      height: 550,
      slices: {
          0: {color: '#00b300'},
          1: {color: '#ff0000'},
          2: {color: '#05386b'},
        },
    titleTextStyle : {
        fontSize : 30, 
    }
  }

  // Display the chart inside the <div> element with id="piechart"
  var chart = new google.visualization.PieChart(document.getElementById('piechart'));
  chart.draw(data, options);
}