import xml.etree.ElementTree as ET
import requests
import urllib
from time import sleep
import time
import random
from tqdm import tqdm

"""
Example:
>> from StreetCompleteNumbers import StreetCompleteNumbers
>> StreetCompleteNumbers("nutzername")
"""



def getUserChangeSets(name, maximum=0):
    """ Maximum gibt die maximale anzahl an 100ern an, die Abgerufen werden"""
    abfragen_anz = 1
    closed_after = ""
    changesets = []
    url = "https://api.openstreetmap.org/api/0.6/changesets?display_name=" + urllib.parse.quote(name) + "&time=2001-01-01"
    ans = requests.get(url)
    try:
        root = ET.fromstring(ans.text)
    except:
        return []
    for child in root:
        cs = child.attrib
        cs["tags"] = {}
        for tagix in range(len(child)):
            tag = child[tagix].attrib
            cs["tags"][tag["k"]] = tag["v"]
        changesets.append(cs)
    ready = False
    try:
        closed_after = root[len(root)-1].attrib["closed_at"]
    except:
        ready = True
    while not ready:
        url = "https://api.openstreetmap.org/api/0.6/changesets?display_name=" + urllib.parse.quote(name) + "&time=2001-01-01," + closed_after
        ans = requests.get(url)
        root = ET.fromstring(ans.text)
        if len(root) < 100:
            ready = True
        for child in root:
            cs = child.attrib
            cs["tags"] = {}
            for tagix in range(len(child)):
                tag = child[tagix].attrib
                cs["tags"][tag["k"]] = tag["v"]
            changesets.append(cs)
        try:
            closed_after = root[len(root)-1].attrib["closed_at"]
        except:
            ready = True
            break
        abfragen_anz += 1
        if (abfragen_anz > maximum and maximum != 0):
            break
        sleep(0.5)
    changesets = cleanChangeSets(changesets)
    return changesets 


def cleanChangeSets(changesets):
    newcss = []
    for cs in changesets:
        schonda = False
        for ncs in newcss:
            if ncs["id"] == cs["id"]:
                schonda = True
        if not schonda:
            newcss.append(cs)
    return newcss

def ChangeSetsToStreetCompleteNumbers(changesets):
    quests = {}
    total = 0
    for changeset in changesets:
        if "StreetComplete:quest_type" in changeset["tags"]:
            if changeset["tags"]["StreetComplete:quest_type"] in quests:
                quests[changeset["tags"]["StreetComplete:quest_type"]] += int(changeset["changes_count"])
            else:
                quests[changeset["tags"]["StreetComplete:quest_type"]] = int(changeset["changes_count"])
    for q in quests:
        total += quests[q]
    print(total)
    return total, quests

def StreetCompleteNumbers(user, maximum=200):
    return ChangeSetsToStreetCompleteNumbers(cleanChangeSets(getUserChangeSets(schlechtesErsetzen(user), maximum)))

def getIDhaeufig(changesets):
    ids = {}
    for changeset in changesets:
        if changeset["id"] in ids:
            ids[changeset["id"]] += 1
        else:
            ids[changeset["id"]] = 1
    return ids

def schlechtesErsetzen(text):
    text = text.replace("Ã¼", "ü")
    text = text.replace("Ã¤", "ä")
    text = text.replace("Ã¶", "ö")
    #text = text.replace("Ã¼", "ü")
    return text

