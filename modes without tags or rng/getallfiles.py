import requests
import os
import datetime
from operator import itemgetter
get = requests.get
curtimeobj = datetime.datetime.now().astimezone(datetime.timezone(datetime.timedelta(hours=0), name="UTC"))
curtime = curtimeobj.strftime("%A %d %B %Y, %H:%M:%S UTC")
total = 0
mlist = []
glist = []
vlist = []
idlist = []
getm = itemgetter(0)
getg = itemgetter(1)
getv = itemgetter(2)
getid = itemgetter(3) 
divider = "-------------------------------------------------------------------------\n"
file = "!noTagsYesRNGmodes.txt"
if os.path.isfile(file) == False: open(file, "x")
with open(file, "w") as f:
    f.write("")
apicall = "https://fnafmml.com/api/maxmodes/list?list=ul&excludedTags=Aim,Awareness,Endurance,Keyboard,Memory,Nerve%20Control,Resource,Sound,Speed,Stamina,Timing"
response = get(apicall)
pages = response.json()["totalPages"]
for page in range(pages):
    response = get(apicall+"&page="+str(page+1))
    pagen = response.json()
    for mode in pagen["maxmodes"]:
        if mode["rng_rating"] != None:
            mlist.append(mode["title"])
            glist.append(mode["game"]["title"])
            vlist.append(mode["list_entry"]["verifier"]["username"])
            idlist.append(mode["id"])
result = list(zip(mlist, glist, vlist, idlist))
for i in range(len(mlist)):
    if i == 0:
        with open(file, "a", encoding="utf-8") as f:
            f.write("Total untagged modes with an RNG rating:"+" "+str(len(mlist))+"\n"+divider)
    with open(file, "a", encoding="utf-8") as f:
        f.write(getm(result[i])+" - "+getg(result[i])+" - "+getv(result[i])+" - "+"https://fnafmml.com/leaderboard/"+getid(result[i])+"\n")
total += len(mlist)
# script 2
tmlist = []
tglist = []
tvlist = []
tidlist = []
mlist = []
glist = []
vlist = []
idlist = []
file = "!noRNGYesTagsmodes.txt"
if os.path.isfile(file) == False: open(file, "x")
with open(file, "w") as f:
    f.write("")
apicall = "https://fnafmml.com/api/maxmodes/list?list=ul&excludedTags=Aim,Awareness,Endurance,Keyboard,Memory,Nerve%20Control,Resource,Sound,Speed,Stamina,Timing"
response = get(apicall)
pages = response.json()["totalPages"]
for page in range(pages):
    response = get(apicall+"&page="+str(page+1))
    pagen = response.json()
    for mode in pagen["maxmodes"]:
        if mode["rng_rating"] == None:
            tmlist.append(mode["title"])
            tglist.append(mode["game"]["title"])
            tvlist.append(mode["list_entry"]["verifier"]["username"])
            tidlist.append(mode["id"])
tempresult = list(zip(tmlist, tglist, tvlist, tidlist))
apicall = "https://fnafmml.com/api/maxmodes/list?list=ul"
response = get(apicall)
pages = response.json()["totalPages"]
for page in range(pages):
    response = get(apicall+"&page="+str(page+1))
    pagen = response.json()
    for mode in pagen["maxmodes"]:
        if mode["rng_rating"] == None and tuple((mode["title"], mode["game"]["title"], mode["list_entry"]["verifier"]["username"], mode["id"])) not in tempresult:
            mlist.append(mode["title"])
            glist.append(mode["game"]["title"])
            vlist.append(mode["list_entry"]["verifier"]["username"])
            idlist.append(mode["id"])
result = list(zip(mlist, glist, vlist, idlist))
for i in range(len(mlist)):
    if i == 0:
        with open(file, "a", encoding="utf-8") as f:
            f.write("Total no RNG rating modes that have tags:"+" "+str(len(mlist))+"\n"+divider)
    with open(file, "a", encoding="utf-8") as f:
        f.write(getm(result[i])+" - "+getg(result[i])+" - "+getv(result[i])+" - "+"https://fnafmml.com/leaderboard/"+getid(result[i])+"\n")
total += len(mlist)
# script 3
mlist = []
glist = []
vlist = []
idlist = []
file = "!noRNGandNoTagsmodes.txt"
if os.path.isfile(file) == False: open(file, "x")
with open(file, "w") as f:
    f.write("")
apicall = "https://fnafmml.com/api/maxmodes/list?list=ul&excludedTags=Aim,Awareness,Endurance,Keyboard,Memory,Nerve%20Control,Resource,Sound,Speed,Stamina,Timing"
response = get(apicall)
pages = response.json()["totalPages"]
for page in range(pages):
    response = get(apicall+"&page="+str(page+1))
    pagen = response.json()
    for mode in pagen["maxmodes"]:
        if mode["rng_rating"] == None:
            mlist.append(mode["title"])
            glist.append(mode["game"]["title"])
            vlist.append(mode["list_entry"]["verifier"]["username"])
            idlist.append(mode["id"])
result = list(zip(mlist, glist, vlist, idlist))
for i in range(len(mlist)):
    if i == 0:
        with open(file, "a", encoding="utf-8") as f:
            f.write("Total modes with no tags and no RNG rating:"+" "+str(len(mlist))+"\n"+divider)
    with open(file, "a", encoding="utf-8") as f:
        f.write(getm(result[i])+" - "+getg(result[i])+" - "+getv(result[i])+" - "+"https://fnafmml.com/leaderboard/"+getid(result[i])+"\n")
total += len(mlist)
print("Total modes that are missing either tags or RNG or both: "+str(total))
# allfile
file = "!all.txt"
with open("!noTagsYesRNGmodes.txt", "r", encoding="utf-8") as f:
    f1 = f.readlines()
with open("!noRNGYesTagsmodes.txt", "r", encoding="utf-8") as f:
    f2 = f.readlines()
with open("!noRNGandNoTagsmodes.txt", "r", encoding="utf-8") as f:
    f3 = f.readlines()
with open(file, "w") as f:
    f.write("")
with open(file, "a", encoding="utf-8") as f:
    f.write("File last updated: "+curtime+"\n")
    f.write("Total modes that are missing either tags or RNG or both: "+str(total)+"\n"+divider)
    f.writelines(f1)
    f.write(divider)
    f.writelines(f2)
    f.write(divider)
    f.writelines(f3)