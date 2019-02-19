place=["adayar","ambathur","guindy"]
dist=[30,40,50]
print("WHERE YOU WANT TO GO?\n 1.adayar 2.ambathur 3.guindy")
choice=int(input())
if choice==1:
    kms=dist[0]
elif choice==2:
    kms=dist[1]
elif choice==3:
    kms=dist[2]
car=["nano","micro","mini","prime"]
amount=[7,9,10,15]
print(" WHICH TYPE OF CAR YOU WANT TO GO?\n 1.nano 2.micro 3.micro 4.prime")
choice=int(input())
if choice==1:
    price=amount[0]
elif choice==2:
    price=amount[1]
elif choice==3:
    price=amount[2]
print(" Estimated amont is",kms*price)

