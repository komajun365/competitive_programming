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

N,M = map(int,input().split())
a = list(map(int,input().split()))
n = 1
while 2 ** n != N:
    n += 1

def get_base(x,basis):
    for b in basis:
        x = min(x,x^b)
    return x

nums = set(range(1,N))
for ai in a:
    nums.remove(ai)

basis = []
basis2 = []
for num in nums:
    x = get_base(num,basis)
    if x != 0:
        basis.append(x)
        basis2.append(num)

if len(basis) < n:
    print(-1)
    exit()

ans = []
now = 0
for i in range(1,N):
    left = 0
    while (i >> left) & 1 == 0:
        left += 1
    go = now ^ basis2[left]
    ans.append('{} {}'.format(now, go))
    now = go

print('\n'.join(ans))

# for 