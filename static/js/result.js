const totalQue = parseInt(document.getElementById("len").value);
const score = parseInt(document.getElementById("score").value); 
const wrongAns = totalQue - score;

// Load google charts
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);



// Draw the chart and set the chart values
function drawChart() {
  var data = google.visualization.arrayToDataTable([
  ['Result','DAA'],
  ['Right Answer',score],
  ['Wrong Answer',wrongAns],
]);

  // Optional; add a title and set the width and height of the chart
  var options = {
      title : "Result",
      is3D: true,
      slices: {
          0: {color: '#00b300'},
          1: {color: '#ff0000'},
        },
    titleTextStyle : {
        fontSize : 30, 
    }
  }

  // Display the chart inside the <div> element with id="piechart"
  var chart = new google.visualization.PieChart(document.getElementById('piechart'));
  chart.draw(data, options);
}

$(window).resize(function(){
  drawChart();
});