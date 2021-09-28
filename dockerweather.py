#
# Get live data from the following sources:
# -City weather data using openweathermap api
#
# Output is send to InfluxDB
# Output is visualized using Grafana
# Use is made of 3 docker containers: InfluxDB, Grafana, this python file
#


import time
from influxdb import InfluxDBClient
from datetime import datetime, timedelta
from outside_weather import outside_weather
from private_info import cities
from private_info import database_name, docker_address, computer_port

time.sleep(5)
client = InfluxDBClient(host=docker_address, port=computer_port)  # connect to Influx 1.8 DB

if __name__ == '__main__':
    dbs = client.get_list_database()
    print('the following databases are found: ', dbs)

    if not any(db['name'] == 'localdata' for db in dbs):
        print('database localdata not found ... creating database')
        client.create_database('localdata')
    else:
        print('database localdata found')
        results = (client.query(database=database_name, query='select * from temperature limit 5'))
        for result in list(results.get_points()):
            print(result)

    while True:
        # get outside weather data from the various cities using open weather site
        data_point = []
        for city in cities:
            data_point = data_point + outside_weather(city)

        client.write_points(data_point, database=database_name)
        print(datetime.now(), data_point)

        time.sleep(60)  # sleep time in sec.
