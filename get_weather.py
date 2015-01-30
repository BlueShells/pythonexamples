#!/usr/bin/env python
# coding=utf-8
import urllib2
import xml.dom.minidom
try:
    url="http://weather.yahooapis.com/forecastrss?u=c&w=2151330"
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    print "Geting data from yahooapis...."
    data = response.read()
    #print data
    dom = xml.dom.minidom.parseString(data)

    root = dom.documentElement
    location = root.getElementsByTagName('yweather:location')
    city = location[0].getAttribute("city")
    weather_conditions=root.getElementsByTagName('yweather:condition')
    weather = weather_conditions[0].getAttribute('text')
    temp = weather_conditions[0].getAttribute('temp')
    print "City:",city
    print "weather:",weather
    print "temp:",temp
except Exception:
    print("there is something wrong")


