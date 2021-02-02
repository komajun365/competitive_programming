# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = list(map(int,input().split()))

ans = [0] * (n+1)
d = dict()
for i,ai in enumerate(a,1):
    if(ai in d):
        d[ai][1] += 1
    else:
        d[ai] = [i,1]
d[0] = [0,0]

a_unique = list(set(a))
a_unique.sort(reverse=True)
a_unique.append(0)

for i in range(len(a_unique)-1):
    num = a_unique[i]
    next = a_unique[i+1]
    head = d[num][0]
    ans[head] += (num-next) * d[num][1]

    d[next][0] = min(d[next][0],d[num][0])
    d[next][1] += d[num][1]

print('\n'.join(map(str,ans[1:])))
