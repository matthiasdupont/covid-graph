<!DOCTYPE html>
<html>
 <head>
   <title>graph</title>
    <script src="./static/Charts.js"></script>
 </head>
 <body>
   <canvas id="myChart"></canvas>
   <script>
    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: {{label}},
        datasets: [{
            label: 'My First dataset',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: {{data}}
        }]
    },

    // Configuration options go here
    options: {}
});
   </script>
 </body>
</html>
