#python 3.6.9

import random
randomlist = []
for i in range(0,10000):
    n = random.randint(1,1000)
    randomlist.append(n)
randomlist.sort()
