#!/usr/bin/python
import json
import urllib
import urllib.request

with open('./openweathermap_conf.json') as f:
  owmfile = json.load(f)

owmWeather = (str(owmfile['owm']['url_weather'])) + (str(owmfile['owm']['str_loc'])) + (str(owmfile['owm']['location'])) + '&' + (str(owmfile['owm']['str_key'])) + (str(owmfile['owm']['apikey']))
owmForecast = (str(owmfile['owm']['url_forecast'])) + (str(owmfile['owm']['str_loc'])) + (str(owmfile['owm']['location'])) + '&' + (str(owmfile['owm']['str_key'])) + (str(owmfile['owm']['apikey']))

print (json.load(urllib.request.urlopen(owmWeather)))
print (json.load(urllib.request.urlopen(owmForecast)))