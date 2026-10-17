import requests
import os
import datetime
get = requests.get
curtimeobj = datetime.datetime.now().astimezone(datetime.timezone(datetime.timedelta(hours=0), name="UTC"))
curtime = curtimeobj.strftime("%A %d %B %Y, %H:%M:%S UTC")
f1 = []
f2 = []
divider = "-------------------------------------------------------------------------\n"
file = "modes with error stats.txt"
if os.path.isfile(file) == False: open(file, "x")
with open(file, "w") as f:
    f.write("")
call = "https://fnafmml.com/api/maxmodes/list?list=ml"
response = get(call)
pages = response.json()["totalPages"]
for page in range(pages):
    response = get(call+"&page="+str(page+1))
    pagen = response.json()["maxmodes"]
    for mode in pagen:
        if mode["avg_length_seconds"] == 0 and "completion_avg_time" not in mode and "calculated_enjoyment" not in mode:
            f1.append("#"+str(mode["ml_rank"])+" (UL rank: #"+str(mode["ul_rank"])+") - "+mode["title"]+" - "+"https://fnafmml.com/leaderboard/"+mode["id"])
call = "https://fnafmml.com/api/maxmodes/list?list=ul"
response = get(call)
pages = response.json()["totalPages"]
for page in range(pages):
    response = get(call+"&page="+str(page+1))
    pagen = response.json()["maxmodes"]
    for mode in pagen:
        if mode["avg_length_seconds"] == 0 and "completion_avg_time" not in mode and "calculated_enjoyment" not in mode:
            f2.append("#"+str(mode["ul_rank"])+" - "+mode["title"]+" - "+"https://fnafmml.com/leaderboard/"+mode["id"])
f = open(file, "a", encoding="utf-8")
f.write("File last updated: "+curtime+"\n")
f.write(divider+"ML:\n"+divider)
for i in range(len(f1)):
    f.write(f1[i]+"\n")
f.write(divider+"UL:\n"+divider)
for i in range(len(f2)):
    f.write(f2[i]+"\n")
f.close()
