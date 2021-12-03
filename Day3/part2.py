from typing import Deque

oxygen = open("imput.txt","r").read().split() # read everthing and split it auto by ' ' and get a list returned with commands and integers

result = []
result2 = []
CO2 = oxygen
x = 0
mm_range = len(oxygen)
while len(oxygen) > 1:
    one,zero = 0,0
    for i in oxygen:    
        if int(i[x:x+1]) == 1:      
            one += 1
        elif int(i[x:x+1]) == 0:
            zero += 1
    if one > zero or one == zero:
        result.append(1)
    else:
        result.append(0)

    oxygen = [ab for ab in oxygen if int(ab[x:x+1]) == result[x]]
    mm_range = len(oxygen)
    x += 1


m_range = len(CO2)
xz = 0
while len(CO2) > 1:
    one,zero = 0,0
    for i in CO2:    
        if int(i[xz:xz+1]) == 1:      
            one += 1
        elif int(i[xz:xz+1]) == 0:
            zero += 1

    if one < zero :
        result2.append(1)
    elif one > zero or one == zero:
        result2.append(0)


    CO2 = [ab for ab in CO2 if int(ab[xz:xz+1]) == result2[xz]]

    m_range = len(CO2) 
    xz +=1

print(int(CO2[0], 2)*int(oxygen[0],2))
