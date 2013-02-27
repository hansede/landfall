#!/usr/bin/python

from pyquery import PyQuery as pq
from lxml import etree
import urllib2


main = pq(url='http://www.wizards.com/Magic/TCG/Article.aspx?x=magic/rules/faqs')
links = main('.article-image')
count = 0

for link in links:
  image = pq(link).attr('src')
  
  if not image.startswith('http://'):
    image = "http://www.wizards.com/" + image
  
  print(image)
  u = urllib2.urlopen(image)
  localFile = open(str(count) + '.gif', 'w')
  localFile.write(u.read())
  localFile.close()
  count += 1
