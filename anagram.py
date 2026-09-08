s='atm'
t='tma'
a=len(s)
b=len(t)
if a==b:
    if sorted(s)==sorted(t):
        print("anagram")
    else:
         print("not anagram")
else:
    print("not anagram")
    
