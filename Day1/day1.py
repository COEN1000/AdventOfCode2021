#Part-1
thingy = open("imput.txt","r").read().split("\n")
count = 0

for i in range(len(thingy)-1):
    if (int(thingy[i+1])) > (int(thingy[i])):
        count += 1
print(count)

#Part-2
thingy = open("imput.txt","r").read().split("\n")
count = 0

for i in range(len(thingy)-3):
    a = int(thingy[i])+int(thingy[i+1])+int(thingy[i+2])
    b = int(thingy[i+1])+int(thingy[i+2])+int(thingy[i+3])

    if a < b:
        count+=1

print(count)
