s='malayalam'
i=0
j=len(s)-1
while i<j:
    if s[i]!=s[j]:
        print("not a palindrome")
        break
    i=i+1
    j=j-1
else:
    print("its palindrome")
        
