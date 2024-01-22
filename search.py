import csv

with open("data.csv","r",newline="") as f:
    c = 0
    reader = csv.reader(f)
    
    name = input("Enter name to be searched:")
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
