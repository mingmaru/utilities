import random
import string

# string.ascii_letters contains both 'a-z' and 'A-Z'
random_char = random.choice(string.ascii_uppercase)
print(random_char)