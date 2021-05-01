import random
import hashlib
import sys
from random import randint

q=62
a=311





random.seed(183703)
print ("\nChoosing Ann Private Key")
ann= random.randint(100,999)
print (ann) 
random.seed(183703)
print ("\nChoosing Barry Private Key")
barry= random.randint(10,99)
print (barry)



A = (q**ann) % a
B = (q**barry) % a



print('\nAnn calculates:')
print('a (Ann  Private Value): ',ann)
print('Ann Public Key (A): ',A,' (g^a) mod p')

print('\nBarry calculates:')
print('b (Barry Private Value): ',barry)
print('Barry Public Key (B): ',B,' (g^b) mod p')

print('\nAnn Session Key:')
keyA=(B**ann) % a
print('Session Key: ',keyA,' (B^a) mod p')
print('Hashed: ',hashlib.sha256(str(keyA).encode()).hexdigest())

print('\nBarry  Session Key:')
keyB=(A**barry) % a
print('Session Key: ',keyB,' (A^b) mod p')
print('Hashed: ',hashlib.sha256(str(keyB).encode()).hexdigest())
