import os

from os import system

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

database={}
def getdata():
        name=input("Enter the bidder name\n")
        amount=input("Enter the bidding amount\n")
        database[name]=amount

def clear():
    # Clears the console screen
    os.system('clear')


while True:
    getdata()

    cont=input("Do you want to continue?||y/n\n")
    if cont=="y":
        clear()
    else:
        print("calculating.....")
        break

result=""
for item in database:
    if database[item]:
        if result=="":
            result=item
        elif int(database[item])>=int(database[result]):
            result=item

print(f"\nThe higest value bidder is {result} with bid of {database[result]}")
