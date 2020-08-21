#!/usr/bin/python
import json
import urllib.request

with open('./openweathermap_conf.json') as f:
  owmfile = json.load(f)
print (owmfile['owm']['apikey'])