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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import bisect

d,l,n, *data = map(int,read().split())
c = data[:d]
kft = data[d:]

days = dict()
for i,ci in enumerate(c):
    if(ci in days):
        days[ci].append(i)
    else:
        days[ci] = [i]

for i,ci in enumerate(c,d):
    days[ci].append(i)

cnt = dict()
cyc = dict()
for key,val in days.items():
    cnt[key] = [0]
    tmp = 0
    m = len(val)
    for i in range(1,m):
        dif = val[i] - val[i-1]
        cnt[key].append(cnt[key][-1] -(-dif // l))
    cyc[key] = [m//2, cnt[key][m//2]]

ans = []
it = iter(kft)
for k,f,t in zip(it,it,it):
    f -= 1
    if(not k in days):
        ans.append(0)
        continue

    if(l >= d):
        if(c[f] == k):
            ans.append(t)
        else:
            ans.append(t-1)
        continue

    rem = t
    eat = 0
    dk = days[k]
    ck = cnt[k]
    i = bisect.bisect_left(dk,f)
    if(dk[i] == f):
        rem -= 1
        eat = 1
    else:
        dif = dk[i] - f
        next = 1-(-dif //l)
        if(next > rem):
            ans.append(0)
            continue
        rem -= next
        eat = 1
    
    cyc_num = rem // cyc[k][1]
    rem -= cyc_num*cyc[k][1]
    eat += cyc_num*cyc[k][0]

    i %= cyc[k][0]
    j = bisect.bisect_left(ck, ck[i] + rem)
    if(ck[j] == ck[i] + rem ):
        eat += j-i
    else:
        eat += j-i-1
    
    ans.append(eat)
    # print(k,f,t,eat)
    # print(dk)
    # print(ck)

print('\n'.join(map(str,ans)))







