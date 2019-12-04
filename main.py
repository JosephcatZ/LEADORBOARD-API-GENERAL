
import requests
import json
from datetime import datetime
def getResponse(url,cookies):
    operUrl = requests.get(url, cookies = cookies,stream = True)
    data = operUrl.raw.read()
    jsonData = json.loads(data)
    return(jsonData)

urlData = "https://adventofcode.com/2019/leaderboard/private/view/[userid].json"
jsonData = getResponse(urlData,{"session":"[session cookie data]]"})
data = jsonData["members"]
for i in(data):
    
    member = data[i]
    print(member["name"]+"'s report")
    print((len(data[i]["name"])+9)*"-")
    print("id:",member["id"])
    print("last star gotten at:",datetime.utcfromtimestamp(int(member["last_star_ts"])).strftime('%Y-%m-%d %H:%M:%S'))
    print("global score:",member["global_score"])
    print("local score:",member["local_score"])
    print("Stars:",member["stars"])
    print("Daily Breakdown:")
    for j in sorted(member["completion_day_level"].keys()):
        new = member["completion_day_level"]
        print("\t Day",str(j)+":")
        for k in sorted(new[j].keys()):
            print("\t\tstar",k,"gotten at:",datetime.utcfromtimestamp(int(new[j][k]["get_star_ts"])).strftime('%Y-%m-%d %H:%M:%S'))
    
    print("\n"*3)