import feedparser
import re
import json

feed = feedparser.parse(
    "https://www.bayern.landtag.de/webangebot2/rss/feed.rss?art=GESETZ&titel=Drucksachen+von+Gesetzentw%C3%BCrfen")
entry = feed.entries[76]

print(entry)

# print(feed)

print(entry["title"])
print("#Link")
print(entry.links[0].href)

print(len(feed.entries))
gesetze = {}

print("----------")
for i in range(len(feed.entries)):
    entry = feed.entries[i]
    gesetze.update({i: {"title": entry.title, "content": entry.summary, "date": entry.published,
                        "mappe": entry.links[0].href, "status": "unbekannt", "beratung": "unbekannt"}})
    if re.match(r"^Gesetzentwurf", entry.title):
        gesetze[i]["status"] = "eingebracht"
    if re.match(r"^Beschlussempfehlung", entry.title):
        gesetze[i]["status"] = "Beschluss empfohlen"
    if re.match(r"^Beschluss zu Gesetzentwurf", entry.title):
        gesetze[i]["status"] = "beschlossen"

    if gesetze[i]["status"] == "eingebracht" or gesetze[i]["status"] == "Beschluss empfohlen":
        gesetze[i]["beratung"] = "aktiv"
    else:
        gesetze[i]["beratung"] = "abgeschlossen"
    print(gesetze[i])

print(gesetze)

with open("gesetze.json", "w") as fp:
    json.dump(gesetze, fp)
"""
for i in range(len(gesetze)):
    if gesetze[i]["status"] == "eingebracht" or gesetze[i]["status"] == "Beschluss empfohlen":
        print(gesetze[i])

"""


