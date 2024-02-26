import json
import requests
import csv


def mapstats(maps):
    lis = []
    for map_id in maps:
        games_played, wins = map_id["gameMode"]["grandPrix"]["gamesPlayed"], map_id["gameMode"]["grandPrix"]["wins"]
        best_time, best_lap = map_id["gameMode"]["timeTrials"]["bestTime"], map_id["gameMode"]["timeTrials"]["bestLap"]
        lis.extend([games_played, wins, best_time, best_lap])
    return lis



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
        maps = data[0]["result"]["data"]["maps"]
        created_at = userdata["created_at"]

        mapdata = mapstats(maps)
        row = [name,uiid,playtime,xp,level,money,driven,drift,skill,created_at]
        row.extend(mapdata)
    
        writer_obj.writerow(row)

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
        wrter.writerow(["name","uiid","playtime","xp","level","money","driven","drift","skill","created_at",'CANYON_games_played', 'CANYON_wins', 'CANYON_best_time', 'CANYON_best_lap', 'VINEYARD_games_played', 'VINEYARD_wins', 'VINEYARD_best_time', 'VINEYARD_best_lap', 'SKI_RESORT_games_played', 'SKI_RESORT_wins', 'SKI_RESORT_best_time', 'SKI_RESORT_best_lap', 'BEACH_games_played', 'BEACH_wins', 'BEACH_best_time', 'BEACH_best_lap'])
        game(lb,wrter,levels)

    print("program executed")
