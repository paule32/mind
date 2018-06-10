import sys
from argparse import ArgumentParser
from xml.dom  import minidom

class AIWeather
	def __init__(self):
		try:
			from urllib.request import urlopen
			from urllib.parse   import urlencode
		except ImportError:
			from urllib import urlopen, urlencode

		API_URL = "http://www.google.com/ig/api?"

	def get(self,loc,unit):
		for location in loc:
			url = API_URL + urlencode({"weather": location})
			xml = urlopen(url).read()
			doc = minidom.parseString(xml)

			forecastinformation = doc.documentElement.getElementsByTagName("forecast_information")[0]
			city		    = forecastinformation.getElementsByTagName("city")[0].getAttribute("data")
			current_conditions  = doc.documentElement.getElementsByTagName("current_conditions")[0]
			temp		    = current_conditions .getElementsByTagName("temp_f" if unit == "F" else "temp_c")[0].getAttribute("data")
			condition	    = current_conditions .getElementsByTagName("condition")[0].getAttribute("data")
			wind_condition	    = current_conditions .getElementsByTagName("wind_condition")[0].getAttribute("data")
			humidity	    = current_conditions .getElementsByTagName("humidity")[0].getAttribute("data")

			indent = "  "
			print("Weather for {0}:".format(city))
			print(indent + "{0}°{1}".format(temp, unit))
			print(indent + condition)
			print(indent + wind_condition)
			print(indent + humidity)
