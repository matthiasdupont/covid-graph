# html-graph
Gets Data from https://github.com/CSSEGISandData/COVID-19.git and displays html chart using charts.js


# Build docker image 
````shell
docker build -t html-graph:0.1 .
````
# run docker image
````shell
docker run -p 8080:8080 html-graph:0.2
````

use http://localhost:8080 on your browser
