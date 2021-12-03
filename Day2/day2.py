#Part 1
test = open("imput.txt","r").read().split("\n") 
depth = 0
horizontal = 0

for i in test:
    mode = i.split(" ")[0]
    amount = int(i.split(" ")[1])

    if mode == "forward":
        horizontal += amount
    elif mode == "up":
        depth -= amount
    elif mode == "down":
        depth += amount
print(horizontal*depth)

#Part 2
test = open("imput.txt","r").read().split("\n") 
depth = 0
horizontal = 0
aim = 0

for i in test:
    mode = i.split(" ")[0]
    amount = int(i.split(" ")[1])

    if mode == "forward":
        horizontal += amount
        depth += amount*aim
    elif mode == "up":
        aim -= amount
    elif mode == "down":
        aim += amount
print(horizontal*depth)
