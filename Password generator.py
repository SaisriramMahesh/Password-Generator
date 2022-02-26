import random
length = int(input("Enter the password length required: ")) # password length required
lower = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,_-"
all = lower + UPPER + numbers + symbols
Password = "".join(random.sample(all, length))
print(Password)