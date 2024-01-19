import json
import requests
import csv

user_stats = {}
levelss = set()
def game(val,writer_obj,text="False"):
    leader_board = json.load(val)
    num = 1

    for player in leader_board[0]["result"]["data"]["rows"]:

        uiid = player['user_id']
        url = f"https://social-api.drift.io/trpc/game.getStats?batch=1&input=%7B%220%22%3A%7B%22id%22%3A%22{uiid}%22%7D%7D"
        respons = requests.get(url)
        
        data = respons.json()
        userdata = data[0]["result"]["data"]["profile"]
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

        print(num)
        num+=1

        levelss.add(data[0]["result"]["data"]["level"]["nextLevelXp"])
        if text and userdata["admin"]:
            text.write(f"Admin spotted lol {uiid}:{name}")
            


if __name__ == "__main__":
    with open("data.json","r") as f:
        
        with open("data.csv","w", encoding="utf-8",newline="") as csvfile:
            wrter = csv.writer(csvfile)
            wrter.writerow(["name","uiid","playtime","xp","level","money","driven","drift","skill","created_at"])

            with open("levellist.txt","w", encoding="utf-8") as levels:
                game(f,wrter,levels)

    print("program executed")