a={14:2,36:3,21:3}
b={19:3,11:5,55:8}
b_c=0
a_c=0
for age,vote in a.items():
    if age>=18:
        a_c+=vote
print(a_c)

for age,vote in b.items():
    if age>=18:
        b_c+=vote
print(b_c)
diff=a_c-b_c
res=abs(diff)
if a_c>b_c:
    print("party a wins")
else:
    print("party b wins")
    
