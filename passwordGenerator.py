import string
import random

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = list(string.ascii_lowercase)
special = ["!", "@", "#", "$", "%", "&", ":"]

next_loop = True

def generate_password(num,spe,password_length):
    password = []
    prange = letters
    if num:
        prange += numbers
    if special:
        prange += special

    for x in range(password_length):
        password.append(prange[random.randint(0, len(prange) - 1)])

    return "".join(password)


while next_loop:
    lenght = int(input("Choose password length"))

    includeNumbers = input("Include numbers? (y/n)")
    if includeNumbers == "y":
        includeNumbers = True
    else:
        includeNumbers = False

    includeSpecial = input("Include special characters? (y/n)")
    if includeSpecial == "y":
        includeSpecial = True
    else:
        includeSpecial = False

    password = generate_password(includeNumbers, includeSpecial, lenght)

    print(password)

    next_loop = input("Continue? (y/n)")
    if next_loop == "y":
        next_loop = True
    else:
        next_loop = False
