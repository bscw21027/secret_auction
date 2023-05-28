import os

auction = {}
a=[]
n = int ( input ( " Enter the number of friends : "))


name = input ( " Enter your name : ")
bid = int ( input ( " Enter your Bid : "))
auction[name] = bid
choice = input ( " Is there a person after You ")
print ("\n")
os.system('cls')

while choice== "yes":
  name = input ( " Enter your name : ")
  bid = int ( input ( " Enter your Bid : "))
  auction[name] = bid
  print ("\n")
  os.system('cls')
        

max_key = max(auction, key=auction.get)
print(max_key)
maxx = max(auction.values())
print(maxx)


print ( f" {max_key} has the maximum bid of {maxx}. He Won! ")







