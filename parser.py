#!/usr/bin/python

from pyquery import PyQuery as pq
from lxml import etree
import urllib
import pymongo
import datetime

from pymongo import Connection
connection = Connection()
landfall = connection.landfall
landfall.drop_collection('releases')
landfall.drop_collection('cards')
landfall.drop_collection('values')
landfall.drop_collection('cardtypes')
landfall.drop_collection('colors')
landfall.drop_collection('rarities')
cards = landfall.cards
values = landfall.values
releases = landfall.releases
types = landfall.types
colors = landfall.colors
rarities = landfall.rarities

def getCardId(cardObj):
  card = cards.find_one(cardObj)

  if card is None:
    cardId = cards.insert(cardObj)
  else: 
    cardId = card["_id"]
    
  return cardId

def getReleaseId(name):
  releaseObj = {'name': name}

  release = releases.find_one(releaseObj)
  
  if release is None:
    releaseId = releases.insert(releaseObj)
  else:
    releaseId = release["_id"]
    
  return releaseId

def getCardTypeId(name):
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

  cardTypeObj = {'name': name}
  myType = types.find_one(cardTypeObj)
  
  if myType is None:
    typeId = types.insert(cardTypeObj)
  else:
    typeId = myType["_id"]
    
  return typeId

def getColorId(name):
  if name is "whtie":
    name = "white"

  colorObj = {'name': name}
  color = colors.find_one(colorObj)
  
  if color is None:
    colorId = colors.insert(colorObj)
  else:
    colorId = color["_id"]
    
  return colorId
  
def getRarityId(name):
  rarityObj = {'name': name}
  rarity = rarities.find_one(rarityObj)
  
  if rarity is None:
    rarityId = rarities.insert(rarityObj)
  else:
    rarityId = rarity["_id"]
    
  return rarityId
    
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
  releaseId = ''
  totalHigh = 0
  totalMedium = 0
  totalLow = 0

  for row in table:
    d = pq(row);
    name = processHtml(d('td > font').html()).lower()
    release = magicSet('body table:first b').html().lower()
    cmc = processHtml(d('td:eq(1) > font').html()).lower()
    cardType = processHtml(d('td:eq(2) > font').html()).lower()
    color = processHtml(d('td:eq(3) > font').html()).lower()
    rarity = processHtml(d('td:eq(4) > font').html()).lower()
    high = parseFloat(processHtml(d('td:eq(5) > font').html()))
    medium = parseFloat(processHtml(d('td:eq(6) > font').html()))
    low = parseFloat(processHtml(d('td:eq(7) > font').html()))
    
    releaseId = getReleaseId(release)
    totalHigh += high
    totalMedium += medium
    totalLow += low

    cardObj = {
      'name': name,
      'release_id': releaseId,
      'cmc': cmc,
      'type_id': getCardTypeId(cardType),
      'color_id': getColorId(color),
      'rarity_id': getRarityId(rarity),
    }

    cardId = getCardId(cardObj)

    value = {
      'valuable_id': cardId,
      'valuable_type': 'Card',
      'high': high,
      'medium': medium,
      'low': low,
      'date': datetime.datetime.utcnow(),
    }

    valueId = values.insert(value)
    cards.update( {"_id": cardId}, {"$push" : {"value_ids" : valueId}} )
    
  value = {
    'valuable_id': releaseId,
    'valuable_type': 'Release',
    'high': totalHigh,
    'medium': totalMedium,
    'low': totalLow,
    'date': datetime.datetime.utcnow(),
  }
  
  valueId = values.insert(value)
  releases.update( {"_id": cardId}, {"$push" : {"value_ids" : valueId}} )
  print("Total : " + str(totalLow))

main = pq(url='http://magic.tcgplayer.com/magic_price_guides.asp')
links = main('a.default_9')
sets = []

for link in links:
  sets.append(pq(link).attr('href'))

for set in sets:
  address = 'http://magic.tcgplayer.com' + set.replace(' ', '%20')
  print("parsing: " + address)
  parseSet(pq(url=address))
