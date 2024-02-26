import csv

class stats:
    all_stats = {'name': 0, 'uiid': 1, 'playtime': 2, 'xp': 3, 'level': 4, 'money': 5, 'driven': 6, 'drift': 7, 'skill': 8, 'created_at': 9, 'CANYON_games_played': 10, 'CANYON_wins': 11, 'CANYON_best_time': 12, 'CANYON_best_lap': 13, 'VINEYARD_games_played': 14, 'VINEYARD_wins': 15, 'VINEYARD_best_time': 16, 'VINEYARD_best_lap': 17, 'SKI_RESORT_games_played': 18, 'SKI_RESORT_wins': 19, 'SKI_RESORT_best_time': 20, 'SKI_RESORT_best_lap': 21, 'BEACH_games_played': 22, 'BEACH_wins': 23, 'BEACH_best_time': 24, 'BEACH_best_lap': 25}
    avg_stats = ["xp","level","money","driven","drift","skill",'CANYON_games_played', 'CANYON_wins', 'CANYON_best_time', 'CANYON_best_lap', 'VINEYARD_games_played', 'VINEYARD_wins', 'VINEYARD_best_time', 'VINEYARD_best_lap', 'SKI_RESORT_games_played', 'SKI_RESORT_wins', 'SKI_RESORT_best_time', 'SKI_RESORT_best_lap', 'BEACH_games_played', 'BEACH_wins', 'BEACH_best_time', 'BEACH_best_lap']
    min_stats = ["CANYON_best_time","CANYON_best_lap","VINEYARD_best_time","VINEYARD_best_lap","SKI_RESORT_best_time","SKI_RESORT_best_lap","BEACH_best_time","BEACH_best_lap"]
    max_stats = ["playtime","xp","level","money","driven","drift","skill","CANYON_games_played","CANYON_wins","VINEYARD_games_played","VINEYARD_wins","SKI_RESORT_games_played","SKI_RESORT_wins","BEACH_games_played","BEACH_wins"]
    # theres probably a better way that my monke brain couldn come up with soo


    def __init__(self,filename):
        '''Pass CSV output from main.py as filename'''

        self.file = open(filename, "r", newline="", encoding="utf-8")
        self.data = csv.reader(self.file)

        self.length = 0
        self.stats = {}
        self.max_stats = {}
        self.min_stats = {}

    def exit(self) -> None :
        self.file.close()
    
    def update_length(self) -> None:
        '''increments self.length'''

        self.length += 1

    def update_max(self, stat, stat_val, username) -> None:
        '''Updates Max list'''
        
        if self.max_stats.get(stat,[0,0])[1] < float(stat_val):
            self.max_stats[stat] = (username, stat_val)

    def update_min(self, stat, stat_val, username) -> None:
        '''Updates Min list'''
        
        if self.min_stats.get(stat,[0,100000000000000000000])[1] > float(stat_val) and (stat_val != 0):
            self.min_stats[stat] = (username, stat_val)

    def update_minmax(self, stat, stat_val, username) -> None:
        if stat in stats.min_stats:
            self.update_min(stat, stat_val, username)
        elif stat in stats.max_stats:
            self.update_max(stat, stat_val, username)

    def update_stat(self, stat, stat_val, username) -> None:
        '''adds stat to self.<stat> and updates minmax_stat'''

        self.stats[stat] = self.stats.get(stat, 0) + stat_val
        self.update_minmax(stat, stat_val, username)

    def get_playtime(self) -> float :
        '''Returns total playtime hours as float'''
        return self.playtime_hours(self.stats["playtime"])
    
    def playtime_hours(self, millis) -> float:
        return millis/(1000*60*60) # pt/1000 to get seconds, 60*60 to get hours
    
    def avg(self, stat) -> float :
        '''returns average of value'''
        return self.stats[stat]/self.length
    
    def max(self, stat) -> tuple:
        return (self.max_stats[stat][0], self.max_stats[stat][1])

    def min(self, stat) -> tuple:
        return (self.min_stats[stat][0], self.min_stats[stat][1])
          
    def output_avg(self) -> str :

        str = ""
        for stat in stats.avg_stats:
            str += f"Average {stat} : {self.avg(stat):.2f}\n"

        return str
    
    def output_max(self) -> str :

        str = ""
        for stat in self.max_stats:
            usernae, val = self.max(stat)
            str += f"Maximum {stat} : {usernae}({val:.2f})\n"
        
        return str
    
    def output_min(self) -> str :

        str = ""
        for stat in self.min_stats:
            usernae, val = self.min(stat)
            str += f"{stat} : {usernae}({val:.2f})\n"
        
        return str
            
    def update(self) -> None:
        '''updates stats or somethign'''

       #shitty code cuz i cba to fix old shitty code

        header = next(self.data)

        for line in self.data:
            for ind, data in enumerate(line):
                if ind not in [0,1,2,9]:
                    self.update_stat(header[ind], float(data), line[0])
                elif ind in [2,12,13,16,17,20,21,24,25]:    
                    self.update_stat(header[ind], self.playtime_hours(int(data)), line[0])

            self.update_length()

    def __repr__(self) -> str:
        avg = self.output_avg()
        max = self.output_max()
        min = self.output_min()
        
        return avg + max + min

    def __str__(self) -> str:
        avg = self.output_avg()
        max = self.output_max()
        min = self.output_min()
        str = f"# Drift.io Stats aggregated\n\n# Average statistics\n{avg}\n\n# Leaderboard\n{max}{min}"

        return str

    def main(self):
        self.update()
        print(self)



if __name__ == "__main__":
    swac = stats("data.csv")

    swac.main()
    
    swac.exit()