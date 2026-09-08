n = 1729
temp = n
temp1=n

sum1=0
rev=0
while temp > 0:
    digit = temp % 10
    sum1=sum1+digit
    temp = temp // 10

temp2=sum1

while temp2> 0:
    digit = temp2 % 10
    rev = rev * 10 + digit
    temp2 = temp2 // 10



result=sum1*rev

if result==n:
    print("good num")
else:
    print("not a good num")

    
