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
f = open('p018_triangle.txt', 'r')
sys.stdin = f

n = 100

ans = 0
done = [False] * (n+1)
for a in range(2,n+1):
    if(done[a]):
        continue
    gr = []
    x = a
    cnt = 1
    while(x <= n):
        done[x] = True
        gr.append(cnt)
        x *= a
        cnt += 1
    cand = set()
    for i in gr:
        for j in range(2,n+1):
            cand.add(i*j)
    ans += len(cand)

print(ans)

cand2 = set()
for a in range(2,n+1):
    for b in range(2,n+1):
        cand2.add(a**b)

print(len(cand2))



'''

'''
