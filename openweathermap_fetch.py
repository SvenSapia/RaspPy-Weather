#!/usr/bin/python
import json
import urllib.request

with open('./openweathermap_conf.json') as f:
  owm = json.load(f)
print(owm)


