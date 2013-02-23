#!/usr/bin/python

from pyquery import PyQuery as pq
from lxml import etree
import urllib
import datetime
import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'root', 'acroman49', 'landfall')

def getCardId(cardObj):
  card = cards.find_one(cardObj)

  if card is None:
    cardId = cards.insert(cardObj)
  else: 
    cardId = card["_id"]
    
  return cardId

def fixCardType(name):
  if "enchantment" in name:
    name = "enchantment"
  elif "nstant" in name:
    name = "instant"
  elif "sorcery" in name:
    name = "sorcery"
  elif "planeswalker" in name:
    name = "planeswalker"
  elif "scheme" in name:
    name = "scheme"
  elif "igpay" in name:
    name = "creature"
  elif "summon" in name:
    name = "creature"
  return name

def fixColor(name):
  if name == "whtie":
    name = "white"
  elif name == "artifact":
    name = "colorless"
  elif name == "land":
    name = "colorless"
  elif name == "":
    name = "colorless"
  elif name == "gold":
    name = "multi"
  return name

def fixValue(value):
  if value == "":
    return "0.00"
  else:
    return value
    
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
  cur = con.cursor()
  table = magicSet('body table:last > tr')

  for row in table:
    d = pq(row);
    name = processHtml(d('td > font').html()).lower().replace("'", "\\'")
    release = magicSet('body table:first b').html().lower().replace("'", "\\'")
    cmc = processHtml(d('td:eq(1) > font').html()).lower()
    cardType = fixCardType(processHtml(d('td:eq(2) > font').html()).lower())
    color = fixColor(processHtml(d('td:eq(3) > font').html()).lower())
    rarity = processHtml(d('td:eq(4) > font').html()).lower()
    high = fixValue(processHtml(d('td:eq(5) > font').html()))
    medium = fixValue(processHtml(d('td:eq(6) > font').html()))
    low = fixValue(processHtml(d('td:eq(7) > font').html()))

    print(name + " : " + low)
    
    cur.execute("insert ignore into rarities(name) values('" + rarity + "')")
    cur.execute("insert ignore into types(name) values('" + cardType + "')")
    cur.execute("insert ignore into colors(name) values('" + color + "')")
    cur.execute("insert ignore into releases(name) values('" + release + "')")

    cur.execute("select id from rarities where name = '" + rarity + "'")
    rarityId = str(cur.fetchone()[0])
    cur.execute("select id from types where name = '" + cardType + "'")
    typeId = str(cur.fetchone()[0])
    cur.execute("select id from colors where name = '" + color + "'")
    colorId = str(cur.fetchone()[0])
    cur.execute("select id from releases where name = '" + release + "'")
    releaseId = str(cur.fetchone()[0])
    
    cur.execute("insert ignore into cards(name, `release`, cmc, type, color, rarity) values('" + name + "', " + releaseId + ", '" + cmc + "', " + typeId + ", " + colorId + ", " + rarityId + ")")
    
    cur.execute("select id from cards where name = '" + name + "' and `release` = " + releaseId)
    cardId = str(cur.fetchone()[0])
    cur.execute("insert into `values`(high, medium, low, card) values('" + high + "', '" + medium + "', '" + low + "', " + cardId + ")")

with con:
  main = pq(url='http://magic.tcgplayer.com/magic_price_guides.asp')
  links = main('a.default_9')
  sets = []

  for link in links:
    sets.append(pq(link).attr('href'))

  for set in sets:
    address = 'http://magic.tcgplayer.com' + set.replace(' ', '%20')
    print("parsing: " + address)
    parseSet(pq(url=address))
