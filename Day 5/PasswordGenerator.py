import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['\ ', '/' ,':' ,'*', '?', '"', '<', '>', '|','@']

nletter = int(input("How many letter you want in your passsword =  \n"))
nnumber=int(input("How many numbers you want in your passpord = \n"))
nsymbol= int(input("How many symbols you want is your password = \n"))
password = ""
for i in range(0,nletter):
    password=password+random.choice(letters)
for i in range(0,nnumber):
    password=password+random.choice(numbers)
for i in range(0,nsymbol):
    password=password+random.choice(symbols)
print(f"Your password can be = {password}")
hardpassword =""
for i in password:
    add = random.choice(password)
    hardpassword = hardpassword+add
    password = password.replace(add,"")
print(f"Hard Password can be = {hardpassword}")
