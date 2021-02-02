from collections import defaultdict
import random

n = 10**7
m = 10**5
d = defaultdict(int)
for i in range(n):
    x = random.randint(0,m)
    y = random.randint(0,m)
    d[x] += y



###############

from collections import defaultdict
import random

n = 10**7
m = 10**5
d = dict()
for i in range(n):
    x = random.randint(0,m)
    y = random.randint(0,m)
    if(x in d):
        d[x] += y
    else:
        d[x] = y


###############

import itertools
from random import randint

n = 1000
for _ in range(n):
    arr = [randint(0,n) for _ in range(n)]
    cumsum = list(itertools.accumulate(arr))

################

from random import randint

n = 1000
for _ in range(n):
    arr = [randint(0,n) for _ in range(n)]
    for j in range(n-1):
        arr[j+1] += arr[j]


##################

n = 5000
l0 = list(range(-1,n+1))
r0 = list(range(1,n+3))
for i in range(n):
    left = l0[::]
    right = r0[::]
