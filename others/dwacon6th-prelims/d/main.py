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

from heapq import heappop,heappush

n = int(input())
a = list(map(int,input().split()))

if n==2:
    print(-1)
    exit()

cnt = [0] * (n+1)
for ai in a:
    cnt[ai] += 1

hq_rem = []
for i in range(1,n+1):
    heappush(hq_rem,i)

hq_cnt = []
for i,ci in enumerate(cnt[1:],1):
    heappush(hq_cnt, -1 * ((ci << 20) + i))

ans = []
use = [0] * (n+1)
minus = [0] * (n+1)
div_num = 1<<20
for i in range(n-3):
    while(hq_cnt):
        count,idx = divmod(-1 * hq_cnt[0], div_num)
        if use[idx] == 1:
            heappop(hq_cnt)
        elif minus[idx] > 0:
            count,idx = divmod(-1 * heappop(hq_cnt), div_num)
            count -= minus[idx]
            minus[idx] = 0
            heappush(hq_cnt, -1 * ((count << 20) + idx))
        else:
            break
    if count == n-i-1:
        ans.append(idx)
        heappop(hq_cnt)
        use[idx] = 1
        minus[a[idx-1]] += 1
        continue
    escape = []
    while(hq_rem):
        cand = heappop(hq_rem)
        if use[cand] == 1:
            continue
        if i != 0 and cand == a[ans[-1]-1]:
            escape.append(cand)
        else:
            ans.append(cand)
            use[cand] = 1
            minus[a[cand-1]] += 1
            break
    for es in escape:
        heappush(hq_rem, es)

rem = []
for i in hq_rem:
    if use[i] == 0:
        rem.append(i)

tail = [n,n,n]
for i,j,k in [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]:
    cand = [rem[i],rem[j],rem[k]]
    if len(ans) == 0:
        if a[cand[0]-1] == cand[1] or a[cand[1]-1] == cand[2]:
            continue
    else:
        if a[ans[-1]-1] == cand[0] or a[cand[0]-1] == cand[1] or a[cand[1]-1] == cand[2]:
            continue
    if tail > cand:
        tail = cand[::]

ans += tail
print(' '.join(map(str,ans)))


    







