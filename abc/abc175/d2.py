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
    now = i
    score = [0]
    while(p[now] != i ):
        now = p[now]
        score.append(score[-1] + c[now])
    cyc_score = score[-1] + c[i]
    cyc = len(score)

    max_loop = k//cyc
    if(cyc_score <= 0):
        tmp = max(score[: min(k+1, cyc)])
    else:
        tmp = max(score) + (max_loop-1)*cyc_score
        tmp = max(tmp, max(score[:(k%cyc) + 1]) + max_loop*cyc_score)

    ans = max(ans,tmp)
print(ans)
