import random as r
from collections import Counter

def main():
    list1 = [r.randint(1,10) for _ in range(10)]
    print(list1) 

    fs = set(list1)

    d1 = dict(a = 1, b = 1, c = 1)
    d2 = {'a':0, 'b':1, 'c':1}

    for key in d2.keys():
        print(key)

    count = Counter(list1); print(count)



main()
