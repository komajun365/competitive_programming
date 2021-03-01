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

from collections import deque

n,m = map(int,input().split())
a = list(map(int,input().split()))

a.sort()

cnt = [1] * m
cnt[0] = n - (m-1)
tot = [0] * m

dqs = [deque() for _ in range(m)]

idx = 0
for i in range(m):
    for j in range(idx, idx+cnt[i]):
        dqs[i].append(a[j])
        tot[i] += a[j]
    idx += cnt[i]

while(True):
    bef = -1
    for i in range(m-1):
        dif = cnt[i] - cnt[i+1]
        if dif == 0:
            continue
        if dif == 1:
            if bef == -1:
                bef = i
                continue
            else:
                change = - tot[bef] + tot[i+1]
                if change <= 0:
                    for k in range(bef,i+1):
                        j = dqs[k].pop()
                        dqs[k+1].appendleft(j)
                        cnt[k] -= 1
                        tot[k] -= j
                        cnt[k+1] += 1
                        tot[k+1] += j
                    bef = -1
                    break
                else:
                    bef = i
                    continue
                       
        bef = -1
        change = - tot[i] + tot[i+1] - dqs[i][-1] * (dif-2)
        if change <= 0:
            j = dqs[i].pop()
            dqs[i+1].appendleft(j)
            cnt[i] -= 1
            tot[i] -= j
            cnt[i+1] += 1
            tot[i+1] += j
            break
    else:
        break

ans = 0
for ci,ti in zip(cnt,tot):
    ans += ci*ti
print(ans)