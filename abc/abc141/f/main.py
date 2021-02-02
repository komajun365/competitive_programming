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

n = int(input())
a = list(map(int,input().split()))

tot = 0
for ai in a:
    tot ^= ai

mask = 2**60 -1 - tot

def get_base(x,basis):
    for b in basis:
        x = min(x,x^b)
    return x

basis = []
for ai in a:
    ai &= mask
    base = get_base(ai,basis)
    if(base!=0):
        basis.append(base)
    
# basis.sort(reverse=True)
add = 0
for b in basis:
    add = max(add, add^b)

print(tot + add*2)



