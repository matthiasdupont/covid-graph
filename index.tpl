<html>
 <head>
   <title>Covid Data graph</title>
    <script src="./static/Charts.js"></script>
 </head>
 <body>
   <div>
     Last update : {{!update_time}}
     <script>
      {{!update_time}}
     </script>
   </div>
   <canvas id="myChart"></canvas>
   <script>
    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: {{!label}},
        datasets:
        [
          {
            label: 'France',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(0, 0, 255)',
            data: {{!data_fr}}
          },
          {
            label: 'US',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(0, 0, 102)',
            data: {{!data_us}}
          }
          ,
          {
            label: 'UK',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(102, 255, 102)',
            data: {{!data_uk}}
          },
          {
            label: 'SP',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 255, 102)',
            data: {{!data_sp}}
          },
          {
            label: 'IT',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 0, 0)',
            data: {{!data_it}}
          }

      ]
    },
    // Configuration options go here
    options: {}
});
   </script>
 </body>
</html>
