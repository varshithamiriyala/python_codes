gender=input()
marks=[1,2,5,6,7,7,3,20]
g_sum=0
b_sum=0
if gender=='g':
    for i in range(len(marks)):
        if i%2==0:
            g_sum+=marks[i]
    print(g_sum)
else:
    for i in range(len(marks)):
        if i%2!=0:
            b_sum+=marks[i]
    print(b_sum)  
    
