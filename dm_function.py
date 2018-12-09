#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:19:39 2018

@author: amir
"""
import ephem #used to calculate sun/moon rise/set. TODO: use novas_py or skyfield
from datetime import date
import requests

def daymoon():
    bochum = ephem.Observer()
    #TODO: use geopy to get lon, lat. Then use LatLon to convert to degrees:min:sec
    bochum.lat = '51:28:54'
    bochum.lon = '7:12:58'
    bochum.date = date.today()
    bochum.horizon = '0:30' #to compensate for obstacles in the horizon

    moon = ephem.Moon()
    #TODO: the following only converts timezone from UTC to local.. make it anywhere
    mr = ephem.localtime(bochum.next_rising(moon)).time()
    ms = ephem.localtime(bochum.next_setting(moon)).time()
    #print('todays moonrise: %s' % mr)

    sun = ephem.Sun()
    sr = ephem.localtime(bochum.next_rising(sun)).time()
    ss = ephem.localtime(bochum.next_setting(sun)).time()
    #print('todays sunrise: %s' % sr)

    dm_start = '-'
    dm_end = '-'
    if mr<ss:
        if mr>sr:
            dm_start = mr
        else:
            dm_start = sr
        if ms>ss:
            dm_end = ss
        else:
            dm_end = ms

    #TODO: make sure this sanity check works for all cases
    if dm_start != '-' and dm_end != '-':
        out_message = 'Today daymoon is visible from %s to %s.\n' % (dm_start, dm_end)
    #    print(out_message)
    else:
        out_message = '--'
    return out_message

def weather(token, lon, lat):
    api_url = 'http://api.openweathermap.org/data/2.5/forecast?lat=%s&lon=%s&APPID=%s' % (lat, lon, token)
    params = {'timeout': 30, 'offset': None}
    resp = requests.get(api_url, params)
    result_json = resp.json()['list'][0]['clouds']['all']
    if result_json < 50:
        message = 'Cloud coverage = %d' % result_json
    else:
        message = '--'
    return message
