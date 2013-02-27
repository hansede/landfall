#!/usr/bin/python

from pyquery import PyQuery as pq
from lxml import etree
import urllib2

count = 1

while True:
  name = pq("http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=" + str(count))('.contentTitle > span').text().lower()
  image = "http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=" + str(count) + "&type=card"
  print(name)
  print(image)
  u = urllib2.urlopen(image)
  localFile = open("cards/" + str(count) + '.jpg', 'w')
  localFile.write(u.read())
  localFile.close()
  count += 1
