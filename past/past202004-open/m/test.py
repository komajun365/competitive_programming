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

# d,l,n, *data = map(int,read().split())
# c = data[:d]
# kft = data[d:]

import random


def calc(d,l,n,c,kft):
    # print(d,l,n)
    # print(c)
    # print(kft)

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

        # print(k,f,t,eat)
        # print(dk)
        # print(ck)


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
        # print(j,i)
        if(ck[j] == ck[i] + rem ):
            eat += j-i
        else:
            eat += j-i-1
        
        ans.append(eat)
        # print(k,f,t,eat)
        # print(dk)
        # print(ck)

    # print('\n'.join(map(str,ans)))


for _ in range(100):
    # d = random.randint(3,10)
    # l = random.randint(3,12)
    # n = random.randint(3,10)
    # c = [random.randint(1,d) for _ in range(d)]
    # kft = []
    # for _ in range(n):
    #     kft.append(random.randint(1,d))
    #     kft.append(random.randint(1,d))
    #     kft.append(random.randint(1,100))

    d,l,n = 10,8,10
    c = [7, 5, 3, 10, 1, 5, 10, 8, 5, 6]
    kft = [1, 2, 36, 8, 7, 90, 3, 1, 21, 5, 3, 32, 10, 7, 2, 7, 10, 96, 7, 6, 17, 9, 1, 97, 10, 3, 70, 1, 9, 16]
    
    calc(d,l,n,c,kft)




