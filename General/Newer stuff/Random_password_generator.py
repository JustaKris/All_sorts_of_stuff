'''
https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
'''

import random
import string

all_of_the_stuff = string.printable


generated_password = []

while not len(generated_password) == 16:
    generated_password.append(str(all_of_the_stuff[random.randint(0, len(all_of_the_stuff))]))

x = ''.join(generated_password)
print(x)

