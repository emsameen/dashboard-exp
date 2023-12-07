from flask import Flask, jsonify
import time
import os
import random
import influxdb_client
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

app = Flask(__name__)
performance_data = {"items": []}

token = os.environ.get("INFLUXDB_TOKEN")
org = "ETAS"
url = "http://localhost:8086"
write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket = "dashboard"


def write_data(timestamp, value):
    write_api = write_client.write_api(write_options=SYNCHRONOUS)

    print(f"{timestamp}, {value}")
    point = Point("performance").tag("timestamp", "value").field(timestamp, value)
    write_api.write(bucket=bucket, org=org, record=point)
    # for value in range(5):
    #     point = (
    #         Point("measurement1").tag("tagname1", "tagvalue1").field("field1", value)
    #     )
    #     write_api.write(bucket=bucket, org="ETAS", record=point)
    #     #time.sleep(1)  # separate points by 1 second


@app.route("/performance", methods=["GET"])
def get_performance_data():
    return jsonify(performance_data)


def generate_data():
    while True:
        timestamp = int(time.time())
        performance_value = random.randint(0, 100)
        # performance_data[timestamp] = performance_value
        item = {
            "time": timestamp,
            "performance": performance_value,
        }
        performance_data["items"].append(item)
        write_data(timestamp, performance_value)
        time.sleep(1)


if __name__ == "__main__":
    import threading

    # Start a thread to generate data in the background
    data_thread = threading.Thread(target=generate_data)
    data_thread.daemon = True
    data_thread.start()

    # Start the Flask app
    app.run(debug=True, host="0.0.0.0", port=8000)
