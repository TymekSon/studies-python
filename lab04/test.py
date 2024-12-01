from collections import defaultdict
from random import randint

dict1 = {'ax':[0,0], 'bx':[0,1], 'cx':[0,2]}

print("dict1: ", dict1)

dict2 = defaultdict(lambda: randint(0, 10))

print("dict2 (default value 0-10): ")
print("examle for key 'dx': ", dict2['dx'])

for i in range(10):
    print(dict2[chr(i+65)])

print(dict2)