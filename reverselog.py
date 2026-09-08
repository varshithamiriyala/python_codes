s='mobile'
s=list(s)
n=len(s)
i=0
j=n-1
while i<j:
   s[i],s[j]=s[j],s[i]
   i=i+1
   j=j-1
print(''.join(s))
