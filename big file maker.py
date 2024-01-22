from scraper import game
import requests
import csv

num = 0
with open("data.csv","w", encoding="utf-8",newline="") as csvfile, open("levellist.txt","w", encoding="utf-8") as levels:
    
    wrter = csv.writer(csvfile)
    wrter.writerow(["name","uiid","playtime","xp","level","money","driven","drift","skill","created_at"])
    
    for offset in range(0,22572,100):
        url = f"https://social-api.drift.io/trpc/leaderboard.get?batch=1&input=%7B%220%22%3A%7B%22type%22%3A%22grand-prix%22%2C%22offset%22%3A{offset}%2C%22limit%22%3A100%7D%7D"
        lb = requests.get(url).json()
        
        num = game(lb,wrter,levels,num)

print("program executed")