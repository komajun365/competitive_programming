# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

class FenwickTree:
    def __init__(self, n: int, mod: int = 0):
        self.__mod = mod
        self.__n = n
        self.__data = [0] * self.__n

    def add(self, p: int, x: int):
        assert (0 <= p) & (p < self.__n)
        if(self.__mod == 0):
            self.__add_mod0(p, x)
        else:
            self.__add_mod(p, x)

    def __add_mod0(self, p: int, x: int):
        p += 1
        while(p <= self.__n):
            self.__data[p - 1] += x
            p += p & -p

    def __add_mod(self, p: int, x: int):
        p += 1
        while(p <= self.__n):
            self.__data[p - 1] += x
            self.__data[p - 1] %= self.__mod
            p += p & -p

    def sum(self, l: int, r: int):
        assert (0 <= l) & (l <= r) & (r <= self.__n)
        if(self.__mod == 0):
            return self.__sum_mod0(r) - self.__sum_mod0(l)
        else:
            return (self.__sum_mod(r) - self.__sum_mod(l)) % self.__mod

    def __sum_mod0(self, r: int):
        s = 0
        while(r > 0):
            s += self.__data[r - 1]
            r -= r & -r
        return s

    def __sum_mod(self, r: int):
        s = 0
        while(r > 0):
            s += self.__data[r - 1]
            s %= self.__mod
            r -= r & -r
        return s

# 計算量オーダーは n = len(a),m= max(a)としてO(nlogm)
def calc_invs(a):
    m = max(a)
    bit = FenwickTree(m+1)
    res = 0
    for i,ai in enumerate(a):
        bit.add(ai,1)
        res += i + 1 - bit.sum(0,ai+1)
    return res

# 座圧する
def calc_invs_compress(a):
    nums = list(set(a))
    nums.sort()
    encode = dict()
    for i,x in enumerate(nums):
        encode[x] = i
    a2 = []
    for ai in a:
        a2.append(encode[ai])
    
    return calc_invs(a2)

n = int(input())
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
a3 = list(map(int,input().split()))

a = []
for i in range(n):
    x1,x2,x3 = a1[i],a2[i],a3[i]
    if x2 % 3 != 2:
        print('No')
        exit()
    
    x = x2//3 + 1
    if x % 2 == i % 2:
        print('No')
        exit()
    
    if x1 == x2-1 and x3 == x2+1:
        a.append(x)
    elif x1 == x2+1 and x3 == x2-1:
        a.append(-1 * x)
    else:
        print('No')
        exit()
    

b = [abs(i) for i in a]
b_even = b[::2]
b_odd = b[1::2]

if calc_invs_compress(b_even) % 2 == 1:
    x = n-1
    if x%2 == 0:
        x -= 1
    b[x] *= -1
if calc_invs_compress(b_odd) % 2 == 1:
    x = n-1
    if x%2 == 1:
        x -= 1
    b[x] *= -1

for i in range(n-2):
    if b[i] != a[i]:
        b[i] *= -1
        b[i+2] *= -1

if a[-2] == b[-2] and a[-1] == b[-1]:
    print('Yes')
else:
    print('No')