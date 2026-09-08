a='success'
res=''
for ch in a:
    if ch not in res:
        res=res+ch
b=sorted(res)
b=''.join(b)
print(b)
