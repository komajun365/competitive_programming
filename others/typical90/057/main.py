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


n,m,*data = map(int,read().split())
mod = 998244353

nums = []
idx = 0
for _ in range(n):
    t = data[idx]
    a = data[idx+1:idx+1+t]
    idx += 1 + t
    tmp = 0
    for ai in a:
        ai -= 1
        tmp += 1<<ai
    nums.append(tmp)

s = data[idx:]
target = 0
for i in range(m):
    if s[i] == 1:
        target += 1<<i


def get_base(x,basis):
    for b in basis:
        x = min(x,x^b)
    return x

basis = []
nouse = 0
for num in nums:
    x = get_base(num,basis)
    if x != 0:
        basis.append(x)
    else:
        nouse += 1

x = get_base(target, basis)
if x != 0:
    print(0)
else:
    print(pow(2,nouse,mod))