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

import sys
read = sys.stdin.buffer.read

n,*uvww = map(int,read().split())
w1s = uvww[2::4]
w2s = uvww[3::4]

xor1 = 0
xor2 = 0
for w1 in w1s:
    xor1 ^= w1
for w2 in w2s:
    xor2 ^= w2
dif = xor1 ^ xor2

def get_base(x,basis):
    for b in basis:
        x = min(x,x^b)
    return x

basis = []
for num in w1s:
    x = get_base(num,basis)
    if x != 0:
        basis.append(x)

x = get_base(dif, basis)
if x != 0:
    print('NO')
    exit()

skip = True
for i in range(n-1):
    w1s[i] ^= dif
w1s.sort()
w2s.sort()
if w1s == w2s:
    print('YES')
else:
    print('NO')