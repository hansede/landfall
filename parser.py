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

def processHtml(html):
  if html is not None:
    return html.replace(u'\xa0', u'').replace('$', '')
  else: return u'';

def parseFloat(text):
  try:
    return float(text)
  except ValueError:
    return float(0)

def parseSet(d):
  table = d('body table:last > tr')

  for row in table:
    d = pq(row);
    name = processHtml(d('td > font').html())
    cmc = processHtml(d('td:eq(1) > font').html())
    cardType = processHtml(d('td:eq(2) > font').html())
    color = processHtml(d('td:eq(3) > font').html())
    rarity = processHtml(d('td:eq(4) > font').html())
    print(processHtml(d('td:eq(5) > font').html()))
    high = parseFloat(processHtml(d('td:eq(5) > font').html()))
    medium = parseFloat(processHtml(d('td:eq(6) > font').html()))
    low = parseFloat(processHtml(d('td:eq(7) > font').html()))

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

sets = []
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Return%20to%20Ravnica")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Avacyn%20Restored")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Dark%20Ascension")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Innistrad")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=New%20Phyrexia")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Mirrodin%20Besieged")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Scars%20of%20Mirrodin")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Rise%20of%20the%20Eldrazi")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Worldwake")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Zendikar")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Alara%20Reborn")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Conflux")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Shards%20of%20Alara")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Eventide")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Shadowmoor")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Morningtide")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Lorwyn")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Future%20Sight")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Planar%20Chaos")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Timeshifted")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Time%20Spiral")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Coldsnap")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Dissension")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Guildpact")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Ravnica")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Saviors%20of%20Kamigawa")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Betrayers%20of%20Kamigawa")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Champions%20of%20Kamigawa")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Fifth%20Dawn")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Darksteel")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Mirrodin")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Scourge")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Legions")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Onslaught")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Judgment")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Torment")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Odyssey")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Apocalypse")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Planeshift")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Invasion")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Prophecy")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Nemesis")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Mercadian%20Masques")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Urza's%20Destiny")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Urza's%20Legacy")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Urza's%20Saga")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Exodus")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Stronghold")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Tempest")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Weatherlight")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Visions")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Mirage")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Alliances")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Homelands")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Ice%20Age")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Fallen%20Empires")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=The%20Dark")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Legends")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Antiquities")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Arabian%20Nights")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Magic%202013%20(M13)")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Magic%202012%20(M12)")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Magic%202011%20(M11)")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Magic%202010")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=10th%20Edition")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=9th%20Edition")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=8th%20Edition")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=7th%20Edition")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Classic%20Sixth%20Edition")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Fifth%20Edition")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Fourth%20Edition")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Revised%20Edition")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Unlimited%20Edition")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Beta%20Edition")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Alpha%20Edition")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=From%20the%20Vault:%20Dragons")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=From%20the%20Vault:%20Exiled")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=From%20the%20Vault:%20Realms")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=From%20the%20Vault:%20Relics")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Duel%20Decks:%20Divine%20vs.%20Demonic")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Duel%20Decks:%20Elspeth%20vs.%20Tezzeret")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Duel%20Decks:%20Elves%20vs.%20Goblins")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Duel%20Decks:%20Garruk%20vs.%20Liliana")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Duel%20Decks:%20Izzet%20vs.%20Golgari")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Duel%20Decks:%20Jace%20vs.%20Chandra")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Duel%20Decks:%20Phyrexia%20vs.%20The%20Coalition")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Premium%20Deck%20Series:%20Slivers")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Premium%20Deck%20Series:%20Fire%20and%20Lightning")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Starter%201999")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Starter%202000")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Portal")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Portal%20Second%20Age")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Portal%20Three%20Kingdoms")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Archenemy")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Battle%20Royale%20Box%20Set")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Beatdown%20Box%20Set")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Chronicles")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Commander")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Planechase")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Planechase%202012")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Unglued")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Unhinged")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Vanguard")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=APAC%20Lands")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Arena%20Promos")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Champs%20Promos")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=European%20Lands")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=FNM%20Promos")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Game%20Day%20Promos")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Gateway%20Promos")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Guru%20Lands")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=JSS/MSS%20Promos")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Judge%20Promos")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Launch%20Party%20Cards")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Magic%20Player%20Rewards")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Media%20Promos")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Prerelease%20Cards")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Pro%20Tour%20Promos")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Release%20Event%20Cards")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=Special%20Occasion")
sets.append("http://magic.tcgplayer.com/db/price_guide.asp?setname=WPN%20Promos")

for set in sets:
  parseSet(pq(url=set))
