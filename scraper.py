import json
import requests
import csv


def game(leader_board,writer_obj,text = False,num = 0):
    
    
    try:
        e_lb = leader_board[0]["result"]["data"]["rows"]
    except Exception as e:
        print(e)
        return num
    
    for player in e_lb:

        uiid = player['user_id']
        url = f"https://social-api.drift.io/trpc/game.getStats?batch=1&input=%7B%220%22%3A%7B%22id%22%3A%22{uiid}%22%7D%7D"
        respons = requests.get(url)
        data = respons.json()
        try:
            userdata = data[0]["result"]["data"]["profile"]
        except Exception as e:
            print(e)
            continue

        name = userdata["username"]
        xp = userdata["experience"]
        playtime = userdata["playtime"]
        drift = userdata["distance_drifted"]
        driven = userdata["distance_driven"]
        money = userdata["coins"]
        skill = userdata["skill_rating"]
        level = data[0]["result"]["data"]["level"]["level"]
        created_at = userdata["created_at"]

        writer_obj.writerow([name,uiid,playtime,xp,level,money,driven,drift,skill,created_at])      

        if userdata["admin"]:
            print(f"Admin spotted lol {uiid}:{name}")
            if text:
                text.write(f"Admin spotted lol {uiid}:{name}")
            

        
        print(num)
        num+=1
    return num



if __name__ == "__main__":
    with open("data.json","r") as f, open("data.csv","w", encoding="utf-8",newline="") as csvfile, open("levellist.txt","w", encoding="utf-8") as levels:
        lb = json.load(f)
        wrter = csv.writer(csvfile)
        wrter.writerow(["name","uiid","playtime","xp","level","money","driven","drift","skill","created_at"])
        game(lb,wrter,levels)

    print("program executed")
