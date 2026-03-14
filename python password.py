import random
import string
upper = string.ascii_uppercase
lower = string.ascii_lowercase
digit = string.digits
symbol ="!@#$%^&*()"
length = int(input("Enter the password length:"))
all_chars = upper + lower + digit + symbol
password = ""
for i in range(length):
     password += random.choice(all_chars)  

print("Generated Password:",password)
