<html>
 <head>
   <title>My Covid Data graph Verion 1.0</title>
   <link rel="stylesheet" href="./static/style.css">
    <script src="./static/Charts.js"></script>
 </head> 
 <body>
   <div id="intro-text">
     <p class="normal_text">
      The Source Data are coming from the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University. <a href="https://github.com/CSSEGISandData/COVID-19">Github Repository</a>
     </p>
   </br>Last update: {{!last_update}}
   </br>
      <script>
      //  print({{!update_time}});
      </script>

        <table border="1">
        <th>Country</th>
        <th>Death</th>
        <th>Confirmed</th>
        <tr>
            <td>France</td>
            <td>{{!last_value_fr}}</td>
            <td>{{!last_value_confirmed_fr}}</td>
        </tr>
        <tr>
            <td>USA</td>
            <td>{{!last_value_us}}</td>
            <td>{{!last_value_confirmed_us}}</td>
        </tr>
        <tr>
            <td>UK</td>
            <td>{{!last_value_uk}}</td>
            <td>{{!last_value_confirmed_uk}}</td>
        </tr>
        <tr>
            <td>Spain</td>
            <td>{{!last_value_sp}}</td>
            <td>{{!last_value_confirmed_sp}}</td>
        </tr>
        <tr>
            <td>Italy</td>
            <td>{{!last_value_it}}</td>
            <td>{{!last_value_confirmed_it}}</td>
        </tr> 
    </table>

    </div>

    <div style="width:95%">
      <canvas id="Progression_france_chart"></canvas>
    </div>

    <div style="width:95%">
      <canvas id="Chart_confirmed"></canvas>
    </div>
    <div style="width:95%">
      <canvas id="progression_us"></canvas>
    </div>

    <div style="width:95%">
      <canvas id="confirmed_us"></canvas>
    </div>

    <div style="width:95%">
      <canvas id="progression_uk"></canvas>
    </div>

    <div style="width:95%">
      <canvas id="confirmed_uk"></canvas>
    </div>

    <div style="width:95%">
      <canvas id="compared_evolution_chart"></canvas>
    </div>

    <div style="width:95%">
      <canvas id="monthly_evolution"></canvas>
    </div>
    <script>
      Chart.defaults.global.title.display = true;
      Chart.defaults.global.title.text = "Pas de Titre";
    </script>

<script type="text/javascript">
  function display_graph(graph_id,graph_data,graph_labels,graph_color,title) 
  {
    var ctx = document.getElementById(graph_id).getContext('2d');
    var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: graph_labels,
        datasets:
        [
          {
            label: title,
            borderColor: graph_color,
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: graph_data,
            pointRadius: 0
          },
        ]
    },
    // Configuration options go here
    options: {
      title:
      {
        text:title
      }
  }});
  }
</script>
   <script>
     display_graph('Progression_france_chart',{{!progression_fr}},{{!label}},'rgb(0, 0, 255)','Mortalité en France (Valeurs lissées sur 7 jours)');
     display_graph('Chart_confirmed',{{!confirmed_data_fr}},{{!label}},'rgb(0, 0, 102)','Nombre de cas confirmés en France (Valeurs lissées sur 7 jours)');
     display_graph('progression_us',{{!progression_us}},{{!label}},'rgb(0, 0, 255)','Mortalité US (Valeurs lissées sur 7 jours)');
     display_graph('confirmed_us',{{!confirmed_data_us}},{{!label}},'rgb(0, 0, 102)','Nombre de cas confirmés US (Valeurs lissées sur 7 jours)');
     display_graph('progression_uk',{{!progression_uk}},{{!label}},'rgb(0, 0, 255)','Mortalité Angleterre (Valeurs lissées sur 7 jours)');
     display_graph('confirmed_uk',{{!confirmed_data_uk}},{{!label}},'rgb(0, 0, 102)','Nombre de cas confirmés Angleterre (Valeurs lissées sur 7 jours)');
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
            data: {{!data_fr}},
            pointRadius: 0
          },
          {
            label: 'US',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(0, 0, 102)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!data_us}},
            pointRadius: 0
          },
          {
            label: 'UK',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(102, 255, 102)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!data_uk}},
            pointRadius: 0
          },
          {
            label: 'SP',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 255, 102)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!data_sp}},
            pointRadius: 0
          },
          {
            label: 'IT',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 0, 0)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!data_it}},
            pointRadius: 0
          }

      ]
    },
    // Configuration options go here
    options: {
      title: {
        text:"Compared evolution of Death (per 1 000 000 inhabitants)"
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
            data: {{!data_month_fr}},
            pointRadius: 0
          },
          {
            label: 'US',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(0, 0, 102)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!data_month_us}},
            pointRadius: 0
          },
          {
            label: 'UK',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(102, 255, 102)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!data_month_uk}},
            pointRadius: 0
          },
          {
            label: 'SP',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 255, 102)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!data_month_sp}},
            pointRadius: 0
          },
          {
            label: 'IT',
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 0, 0)',
            backgroundColor: 'rgba(0, 0, 0, 0)',
            data: {{!data_month_it}},
            pointRadius: 0
          }

      ]
    },
    // Configuration options go here
    options: {
      title: {
        text:"Last 2 Months compared death evolution (per 1 000 000 inhabitants)"
      }
    }
});
   </script>
 </body>
</html>
