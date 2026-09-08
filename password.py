passw='Varshitha@28'
if len(passw)>8:
    uc=0
    lc=0
    sc=0
    dc=0
for ch in passw:
    if ch.isupper():
        uc+=1
    elif ch.islower():
        lc+=1
    elif ch.isdigit():
         dc+=1
    else:
         sc+=1
if uc>0 and lc>0 and sc>0 and dc>0:
    print("strong")
else:
    print("weak")
    
