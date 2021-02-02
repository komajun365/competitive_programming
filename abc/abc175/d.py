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

n,k = map(int,input().split())
p = list(map(lambda x: int(x)-1,input().split()))
c = list(map(int,input().split()))

ans = max(c)
if(ans <= 0):
    print(ans)
    exit()

for i in range(n):
    if(i == p[i]):
        tmp = max(c[i], c[i]*k)
        ans = max(ans,tmp)
        continue

    now = p[i]
    score = [c[now]]
    while(p[now] != i ):
        now = p[now]
        score.append(score[-1] + c[now])
    cyc_score = score[-1] + c[i]
    cyc = len(score)

    tmp = max(score[:(k%cyc) + 1])
    tmp += max(0,cyc_score) * (k//cyc)
    ans = max(ans,tmp)
print(ans)
