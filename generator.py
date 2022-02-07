import random, string

# sets var letters to print out randmom string using .ascii_letters
# .ascii_letters prints out letters in both upper case and lower case
letters = string.ascii_letters
print ( ''.join(random.choice(letters) for i in range(10)) )

## generates random ingeter from 0-5
n = random 
n = random.randint(0,5)
print(n)
