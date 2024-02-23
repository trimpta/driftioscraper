import csv

class stats:

    def __init__(self,filename):
        '''Pass CSV output from main.py as filename'''

        self.file = open(filename, "r", newline="")
        self.data = csv.reader(self.file)

        self.length = 0
        # self.play_time = 0
        # self.total_level = 0
        # self.total_xp = 0
        # self.total_money = 0
        # self.total_skill = 0
        # self.distance_driven = 0
        # self.distance_drifted = 0
        self.stats = {}
        self.max_stats = {}
        self.adminlist = {}

    def exit(self) -> None :
        self.file.close()
    
    def add_admin(self, uuid, username) -> None:
        '''update self.adminlist'''

        self.adminlist[username] = uuid   

    def update_length(self) -> None:
        '''increments self.length'''

        self.length += 1

    def update_stat(self, stat, stat_val, username) -> None:
        '''adds stat to self.<stat> and updates max_stats if needed'''

        if self.max_stats.get(stat,[0,0])[1] < float(stat_val):
            self.max_stats[stat] = (username, stat_val)

        self.stats[stat] = self.stats.get(stat, 0) + stat_val

    def get_playtime(self) -> float :
        '''Returns total playtime hours as float'''
        return self.playtime_hours(self.stats["playtime"])

        
    
    @staticmethod
    def playtime_hours(millis) -> float:
        return millis/(1000*60*60) # pt/1000 to get seconds, 60*60 to get hours

    
    def avg(self, stat) -> float :
        '''returns average of value'''
        return self.stats[stat]/self.length
    
    def output_avg(self) -> str :

        str = ""
        
        for stat in ["xp","level","money","driven","drift","skill"]:
            str += f"Average {stat} : {self.avg(stat)}\n"

        
        return str
    
    def output_max(self) -> str :

        str = ""

        for stat in self.max_stats:
            usernae, val = self.max_stats[stat][0], self.max_stats[stat][1]
            str += f"Maximum {stat} : {usernae}({val})\n"

        # str = self.max_stats
        
        return str

    
    def __repr__(self) -> str:
        avg = self.output_avg()

        max = self.output_max()
        
        return avg + max

    def __str__(self) -> str:
        avg = self.output_avg()

        max = self.output_max()

        str = f"# Drift.io Stats aggregated\n\n# Average statistics\n{avg}\n\n# Maximum statistics\n{max}"

        return str
        

    def update(self) -> None:
        '''updates stats or somethign'''

        #["name","uiid","playtime","xp","level","money","driven","drift","skill","created_at"]
        #shitty code cuz i cba to fix old shitty code

        header = next(self.data)

        for line in self.data:
            for ind, data in enumerate(line):
                if ind not in [0,1,2,9]:
                    self.update_stat(header[ind], float(data), line[0])
                # elif ind == 2:
                    # self.update_stat(header[ind], self.playtime_hours(int(data)), line[2])


        
            self.update_length()


    def main(self):

        self.update()
        
        print(self)



if __name__ == "__main__":
    swac = stats("data.csv")

    swac.main()

    swac.exit()