#!/usr/bin/python

from pyquery import PyQuery as pq
from lxml import etree
import urllib
import pymongo
import datetime

from pymongo import Connection
connection = Connection()
landfall = connection.landfall
#landfall.drop_collection('cards')
cards = landfall.cards

def processHtml(html):
  if html is not None:
    return html.replace(u'\xa0', u'').replace('$', '')
  else: return u'';

def parseFloat(text):
  try:
    return float(text)
  except ValueError:
    return float(0)

def parseSet(magicSet):
  table = magicSet('body table:last > tr')

  for row in table:
    d = pq(row);
    name = processHtml(d('td > font').html())
    release = magicSet('body table:first b').html()
    cmc = processHtml(d('td:eq(1) > font').html())
    cardType = processHtml(d('td:eq(2) > font').html())
    color = processHtml(d('td:eq(3) > font').html())
    rarity = processHtml(d('td:eq(4) > font').html())
    high = parseFloat(processHtml(d('td:eq(5) > font').html()))
    medium = parseFloat(processHtml(d('td:eq(6) > font').html()))
    low = parseFloat(processHtml(d('td:eq(7) > font').html()))

    cardObj = {
      'name': name,
      'release': release,
      'cmc': cmc,
      'type': cardType,
      'color': color,
      'rarity': rarity,
    }

    card = cards.find_one(cardObj)

    if card is None:
      cardId = cards.insert(cardObj)
    else: 
      cardId = card["_id"]

    value = {
      'high': high,
      'medium': medium,
      'low': low,
      'date': datetime.datetime.utcnow(),
    }

    cards.update( {"_id": cardId}, {"$push" : {"values" : value}} )
    print(name + " : " + str(low))

main = pq(url='http://magic.tcgplayer.com/magic_price_guides.asp')
links = main('a.default_9')
sets = []

for link in links:
  sets.append(pq(link).attr('href'))

for set in sets:
  address = 'http://magic.tcgplayer.com' + set.replace(' ', '%20')
  print("parsing: " + address)
  parseSet(pq(url=address))
