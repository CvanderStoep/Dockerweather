# Home Automation Project 
(OPENWEATHERMAP, INFLUXDB, GRAFANA, DOCKER, DOCKER COMPOSE)
### Get live data from the following sources:
* City weather data using openweathermap api (real-time data)

### Output is send to InfluxDB
### Output is visualized using Grafana
* The grafana-carlo image contains the dashboard (import the json file)
* The influxdb-carlo image contains some existing prerecorded data (copy data files)
* the dockerweather image contains the python file to collect weather info


### Commands to run:
* folder dockergrafana:
* docker build -t grafana-carlo -f Dockerfile . (note the dot at the end)
* folder dockerinfluxdb
* docker build -t influxdb-carlo -f Dockerfile .
* folder Dockerweather
* docker compose up --build

* view the grafana dashboard: localhost:3000
* admin - admin
* 