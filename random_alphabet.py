import random
import string

# string.ascii_letters contains both 'a-z' and 'A-Z'
# Use string.ascii_lowercase for just lower case
random_char = random.choice(string.ascii_uppercase)
print(random_char)