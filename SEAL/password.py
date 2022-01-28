import random
import string
print("Hello, welcome to the random password generator!!")

all_letters = string.ascii_letters

lower = all_letters[0:len(all_letters)//2]  # lowercase letters

upper = all_letters[len(all_letters)//2:]  # uppercase letters

numbers = string.digits  # numbers

symbols = string.punctuation  # symbols

mixed = lower + upper + numbers + symbols

length = int(input("Enter the size of the password: "))

password = random.sample(mixed, length)

password = "".join(password)

print("Password =", password)



