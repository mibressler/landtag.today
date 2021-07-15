
import feedparser
import re
import json
import urllib.request


def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()


def shortTitle(str):
        short = str
        if re.match(r"^zur", short) or re.match(r"^für", short):
                short = short[3:len(short)]
        if re.match(r"^über", short):
                short = short[4:len(short)]
        return short


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
    gesetze.update({i: {"title": entry.title, "content": entry.summary, "date": entry.published_parsed,
                        "mappe": entry.links[0].href, "status": "unbekannt", "beratung": "unbekannt","shorttitle":shortTitle(entry.summary)}})
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
    download_file(gesetze[i]["mappe"],str(i))

print(gesetze)

def dumpAll(allgesetze):
        with open("gesetze.json", "w") as fp:
                json.dump(allgesetze, fp)


print("SO")
print(gesetze)
print("SO")
def dumpActive(actgesetze):
        print(gesetze)
        print("SAVE")
        for i in range(len(actgesetze)):
                if actgesetze[i]["beratung"]!="aktiv":
                        actgesetze.pop(i)
        with open("gesetze_active.json", "w") as fp:
                 json.dump(actgesetze, fp)
        print("WO")
        print(actgesetze)
        print(gesetze)
        return


def dumpInActive(ingesetze):
        for i in range(len(ingesetze)):
                try:
                    if ingesetze[i]["beratung"]!="abgeschlossen":
                        ingesetze.pop(i)
                finally:
                    print("n")
        with open("gesetze_vorbei.json", "w") as fp:
                json.dump(ingesetze, fp)
        return



dumpAll(gesetze)
# dumpActive(gesetze)


#print(gesetze)
#dumpInActive(gesetze)


"""
for i in range(len(gesetze)):
    if gesetze[i]["status"] == "eingebracht" or gesetze[i]["status"] == "Beschluss empfohlen":
        print(gesetze[i])

"""


