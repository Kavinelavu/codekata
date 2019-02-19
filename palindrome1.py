e=int(raw_input())
c=e
rev=0
while c!=0:
    rev=(rev*10)+(c%10)
    c=c//10
if e==rev:
    print("yes")
else:
    print("no")
