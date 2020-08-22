#!/usr/bin/python
import json
import urllib
import urllib.request

with open('./openweathermapConf.json') as f:
  owmConf = json.load(f)
f.close()

owmWeatherURL = (str(owmConf['owm']['url_weather'])) + (str(owmConf['owm']['str_loc'])) + (str(owmConf['owm']['location'])) + '&' + (str(owmConf['owm']['str_key'])) + (str(owmConf['owm']['apikey']))
owmForecastURL = (str(owmConf['owm']['url_forecast'])) + (str(owmConf['owm']['str_loc'])) + (str(owmConf['owm']['location'])) + '&' + (str(owmConf['owm']['str_key'])) + (str(owmConf['owm']['apikey']))

with open('./openweathermapWeather.json','w') as f:
  f.write(str(json.load(urllib.request.urlopen(owmWeatherURL))))
f.close()

with open('./openweathermapForecast.json','w') as f:
  f.write(str(json.load(urllib.request.urlopen(owmForecastURL))))
f.close()