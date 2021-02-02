# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討12分　実装8分 バグとり7分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m = map(int,readline().split())
data = list(map(int,read().split()))

it = iter(data[:2*n])
sv = [0] * n
for i,(s,v) in enumerate(zip(it,it)):
    sv[i] = (v,s)
sv.sort(reverse=True)

c = data[2*n:]
c.sort(reverse=True)

ans = 0
i = 0
for size in c:
    while(i < n):
        v,s = sv[i]
        i += 1
        if(size >= s):
            ans += 1
            break

print(ans)
