n = 9999
temp = str(n)

while len(temp) != 1:
    sum = 0

    for i in temp:
        sum = sum + int(i)

    temp = str(sum)

print(temp)

