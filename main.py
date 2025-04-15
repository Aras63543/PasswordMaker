import random
import string

length = 15

characters = string.punctuation + string.hexdigits 

password = ""
for i in range(length):
    random_character = random.choice(characters)
    password = password + random_character

print("Your password is: " + password)
