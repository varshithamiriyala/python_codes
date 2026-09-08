s="ra cecar"
s=s.replace(' ',''0)
rev=""
for i in s:
    rev=i+rev
if s==rev:
    print("its palindrome")
else:
    print("its not palindrome")

##if s==s[::-1]:
##    print("its palindrome")
##else:
##    print("its not  palindrome")
   
