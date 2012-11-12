#!/usr/bin/python

from pyquery import PyQuery as pq
from lxml import etree
import urllib
import pymongo

from pymongo import Connection
connection = Connection()
landfall = connection.landfall
landfall.drop_collection('cards')
cards = landfall.cards

fileString = open('returntoravnica.html', 'r').read()
d = pq(fileString)
table = d('body table:last > tr')

for row in table:
  d = pq(row);
  name = d('td > font').html().replace(u'\xa0', u'')
  cmc = d('td:eq(1) > font').html().replace(u'\xa0', u'')
  cardType = d('td:eq(2) > font').html().replace(u'\xa0', u'')
  color = d('td:eq(3) > font').html().replace(u'\xa0', u'')
  rarity = d('td:eq(4) > font').html().replace(u'\xa0', u'')
  high = d('td:eq(5) > font').html().replace(u'\xa0', u'').replace('$', '');
  medium = d('td:eq(6) > font').html().replace(u'\xa0', u'').replace('$', '');
  low = d('td:eq(7) > font').html().replace(u'\xa0', u'').replace('$', '');

  card = {
    'name': name,
    'cmc': cmc,
    'type': cardType,
    'color': color,
    'rarity': rarity,
    'high': high,
    'medium': medium,
    'low': low,
  }

  cards.insert(card)
  print(card)
