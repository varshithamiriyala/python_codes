nums=[4, 1,2,4,3,3,2,1,4,4]
d={}
for i in nums:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    print(i,":",d[i])

print(d)

    
    
