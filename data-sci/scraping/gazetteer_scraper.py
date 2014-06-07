#!/usr/bin/env python
"""
Settle HK Gazetteer Scraper
"""
from __future__ import division
import urllib2
import os
import json

DATA_DIR = 'data/'

sources = [
  {
    'url':'http://137.189.97.90:5901/api/?projector=region,district,area,table,row,column,value&return=data&skip=0',
    'output':'gazetteer_raw_data.json'
  },
  {
    'url':'http://gazetteer.hk/locale/en-US/generated_ns-translation.json',
    'output':'gazetteer_map.json'
  }
]

for source in sources:

  # Check if file exists already
  if not os.path.isfile(DATA_DIR+source['output']):
    print source['output'] + ' doesnt eixst, downloading...'
    # If not, download data from the API
    json_data = urllib2.urlopen(source['url'])

    data = json.load(json_data)
    if 'data' in data:
      data = data['data']
    with open(DATA_DIR+source['output'], 'w') as outfile:
      json.dump(data, outfile)

  else:
    print source['output'] + ' already exists'

print 'Completed'




