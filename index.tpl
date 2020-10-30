<html>
 <head>
   <title>Covid Data graph</title>
   <link rel="stylesheet" href="./static/style.css">
    <script src="./static/Charts.js"></script>
 </head>
 <body>
   <div id="intro-text">
     <p class="normal_text">
       Source: Center for Systems Science and Engineering (CSSE) at Johns Hopkins University <a href="https://github.com/CSSEGISandData/COVID-19">Github Repository</a>
     </p>
   </br>Last update: {{!update_time}}
      <script>
        {{!update_time}}
      </script>
    </br>  Last value france: {{!last_value_fr}}
    </br>  Last value US: {{!last_value_us}}
    </br>  Last value UK: {{!last_value_uk}}
    </br>  Last value Spain: {{!last_value_sp}}
    </br>  Last value Italy: {{!last_value_it}}
    </div>

    <div style="width:75%">
      <canvas id="Progression_france_chart"></canvas>
    </div>

    <div style="width:75%">
      <canvas id="Chart_confirmed"></canvas>
    </div>

    <div style="width:75%">
      <canvas id="compared_evolution_chart"></canvas>
    </div>

    <div style="width:75%">
      <canvas id="monthly_evolution"></canvas>
    </div>
    <script>
      Chart.defaults.global.title.display = true;
      Chart.defaults.global.title.text = "Pas de Titre";
    </script>

   <script>
    var ctx = document.getElementById('Progression_france_chart').getContext('2d');
    var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: {{!label}},
        datasets:
        [
          {
            label: 'death France',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(0, 0, 255)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!progression_fr}}
          },
        ]
    },
    // Configuration options go here
    options: {
      title: {
        text:"Death Evolution in France"
      }
    }
});
   </script>

   <script>
    var ctx = document.getElementById('Chart_confirmed').getContext('2d');
    var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: {{!label}},
        datasets:
        [
          {
            label: 'confirmed France',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(0, 0, 102)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!confirmed_data_fr}}
          }
        ]
    },
    // Configuration options go here
    options: {
      title: {
        text:"Evolution of confirmed cases in France"
      }
    }
});
   </script>

   <script>
    var ctx = document.getElementById('compared_evolution_chart').getContext('2d');
    var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: {{!label}},
        datasets:
        [
          {
            label: 'fr',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(0, 0, 255)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!data_fr}}
          },
          {
            label: 'US',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(0, 0, 102)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!data_us}}
          },
          {
            label: 'UK',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(102, 255, 102)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!data_uk}}
          },
          {
            label: 'SP',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 255, 102)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!data_sp}}
          },
          {
            label: 'IT',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 0, 0)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!data_it}}
          }

      ]
    },
    // Configuration options go here
    options: {
      title: {
        text:"Compared evolution of Death (per 10 000 inhabitants)"
      }
    }
});
   </script>

   <script>
    var ctx = document.getElementById('monthly_evolution').getContext('2d');
    var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: {{!month_label}},
        datasets:
        [
          {
            label: 'fr',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(0, 0, 255)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!data_month_fr}}
          },
          {
            label: 'US',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(0, 0, 102)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!data_month_us}}
          },
          {
            label: 'UK',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(102, 255, 102)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!data_month_uk}}
          },
          {
            label: 'SP',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 255, 102)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!data_month_sp}}
          },
          {
            label: 'IT',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 0, 0)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!data_month_it}}
          }

      ]
    },
    // Configuration options go here
    options: {
      title: {
        text:"Last 2 Months compared death evolution (per 10 000 inhabitants)"
      }
    }
});
   </script>
 </body>
</html>
