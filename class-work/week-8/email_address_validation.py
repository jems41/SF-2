'''
--> take a gmail address and add a + 
and a string before the @ symbol and the
email address is still valid

--> dots vefore the @ symbol are ignored
lou.is.is.ut
--> uppercase and lowercase differences througout
the addressses are ignored 
LouiSa ...


Given email addresses by the user,
determine the number of unique addresses.

--> characters from + to @ ignored
-->dots before @ ignored
--> cases are also ignored(upper and lower)

INPUT SPEC:
--> First line contains integer n, number of lines
red from usr
--> next n lines, actual email addrsses
  --> each email addresse consists of at least

  --> 
  --> output:
  number of unique emails addrs
'''
def clean(address):
    #1. Remove anything between '+' and @
    plus_index = address.find('+')
    if plus_index != -1:
        at_index = address.find('@')
        address = address[:plus_index] + address[at_index:]
    

    #2. Remove dots before @
    at_index = address.find('@')
    address = address[:at_index].replace('.','') + address[at_index:]
    #3. make everything same case
    address = address.lower()

    return address
#TODO
# read input from the usr
n = int(input('number of addrs'))
addresses = set()
for i in range(n):
    address = input()
    
#TODO
#clean each email addrs
    address = clean(address)
#TODO
#collect all clean addrs in a list
    #if address not in addresses:
    addresses.add(address)
#TODO
#return length of clean list
print(len(addresses))