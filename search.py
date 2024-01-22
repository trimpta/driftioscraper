import csv
import sys

if len(sys.argv) == 0:
    name = input("Enter name to be searched:")
else:
    name = sys.argv[-1]

with open("data.csv","r",newline="") as f:
    c = 0
    reader = csv.reader(f)
    
    print("Search results:")
    print("Name \t\t\t\t\tUUID")
    for line in reader:
        if name == line[0].lower():
            print(f"{line[0]} \t\t\t\t{line[1]}")
            c = 1
            break
        if name.lower() in line[0].lower():
            print(f"{line[0]} \t\t\t\t{line[1]}")
            c += 1
    print(f"total count: {c}")
    if not c:
        print("User doesn't exist in records")