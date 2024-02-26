from scraper import game
import requests
import csv


headers = []

for mapname in ["CANYON", "VINEYARD", "SKI_RESORT", "BEACH"]:
    for datatype in ["games_played", "wins", "best_time", "best_lap"]:
        headers.append(f"{mapname}_{datatype}")

num = 0
with open("data.csv","w", encoding="utf-8",newline="") as csvfile, open("levellist.txt","w", encoding="utf-8") as levels:
    
    wrter = csv.writer(csvfile)
    wrter.writerow(["name","uiid","playtime","xp","level","money","driven","drift","skill","created_at",'CANYON_games_played', 'CANYON_wins', 'CANYON_best_time', 'CANYON_best_lap', 'VINEYARD_games_played', 'VINEYARD_wins', 'VINEYARD_best_time', 'VINEYARD_best_lap', 'SKI_RESORT_games_played', 'SKI_RESORT_wins', 'SKI_RESORT_best_time', 'SKI_RESORT_best_lap', 'BEACH_games_played', 'BEACH_wins', 'BEACH_best_time', 'BEACH_best_lap'])
    for offset in range(0,500,100):
        url = f"https://social-api.drift.io/trpc/leaderboard.get?batch=1&input=%7B%220%22%3A%7B%22type%22%3A%22grand-prix%22%2C%22offset%22%3A{offset}%2C%22limit%22%3A100%7D%7D"
        lb = requests.get(url).json()
        
        num = game(lb,wrter,levels,num)

print("program executed")