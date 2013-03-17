#!/usr/bin/python

from pyquery import PyQuery as pq
from lxml import etree
import urllib2

count = 137045

while count <= 1000000:
  print(count)
  text = pq("http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=" + str(count))('.contentTitle > span').text()
  
  if text is None:
    count += 1
    continue
    
  name = text.lower()
  image = "http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=" + str(count) + "&type=card"
  print(name)
  print(image)
  u = urllib2.urlopen(image)
  localFile = open("cards/" + str(count) + '.jpg', 'w')
  localFile.write(u.read())
  localFile.close()
  count += 1
  
#3756
#3757
#4312
#4669
#4694
