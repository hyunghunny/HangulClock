# coding=UTF-8

# @brief {brief description]
#
# @author webofthink@snu.ac.kr
#
# from http://flask.pocoo.org/ tutorial
from flask import Flask
from weather import getKoreaWeather
from weather import getNearbyWeather
import json

app = Flask(__name__)

@app.route("/") # take note of this decorator syntax, it's a common pattern
def hello():
    return "Hello World!"

@app.route("/api/")
def billboard():
    return "Under construction"


@app.route("/api/weathers/")
def weather():
    weatherInfo = getNearbyWeather()
    print weatherInfo
    return json.dumps(weatherInfo)

@app.route("/api/weathers/<location>/")
def weatherByLocation(location):
    weatherInfo = getKoreaWeather(location)
    print weatherInfo
    return json.dumps(weatherInfo)

if __name__ == "__main__":
    app.run()
