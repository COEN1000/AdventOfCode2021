test = open("imput.txt","r").read().split() 
one,zero = [0]*len(test[0]),[0]*len(test[0])

for bits in test:
    bit = next(iter(most_common(bits)))


for i in test:
    for x in range(len(one)):
        if int(i[x:x+1]) == 1:
            one[x] += 1       
        elif int(i[x:x+1]) == 0:
            zero[x] += 1

answer,inverted = '',''
for a in range(len(zero)):
    if one[a] > zero[a]:
        inverted += '0'
        answer += '1'
    else:
        answer += '0'
        inverted += '1'
print("AOC day3 pt1: {}".format(int(answer,2) * int(inverted,2)))