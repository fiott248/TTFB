#!/bin/python
#written by Daniel Fiott
import urllib2
from time import time
from urllib2 import urlopen as open
from urllib2 import Request as req
from sys import argv
script, url = argv
openurl = urllib2.build_opener()

#set headers
request = req(url, headers={'User-Agent' : "speedtest"})
#set request
stream = open( request )
#check current time
start = time()
#open request
respond = openurl.open(request)
#read fist Byte 
respond.read(1)
#Start time minus the time of first byte
ttfb = time() - start
#close connection (so script does not need to download all page to finish
respond.close()
#print output
print(round(ttfb,3))
