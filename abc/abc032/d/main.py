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

n,w,*data = map(int,read().split())

vw = []
it = iter(data)
for x,y in zip(it,it):
    vw.append([x,y])

max_v = 0
max_w = 0
for vi,wi in vw:
    max_v = max(max_v,vi)
    max_w = max(max_w,wi)

if max_v <= 1000:
    inf = 10**15
    m = max_v*n
    dp = [inf] * (m+1)
    dp[0] = 0
    for vi,wi in vw:
        next = [inf] * (m+1)
        for j in range(m+1):
            if j >= vi:
                next[j] = min(next[j], dp[j], dp[j-vi] + wi)
            else:
                next[j] = min(next[j], dp[j])
        dp, next = next, dp
    
    ans = 0
    for i,wi in enumerate(dp):
        if wi <= w:
            ans = i
    print(ans)

elif max_w <= 1000:
    m = min(max_w*n,w)
    dp = [0] * (m+1)
    for vi,wi in vw:
        next = [0] * (m+1)
        for j in range(m+1):
            if j >= wi:
                next[j] = max(next[j], dp[j], dp[j-wi] + vi)
            else:
                next[j] = max(next[j], dp[j])
        dp, next = next, dp
    
    print(max(dp))

elif n <= 30:
    if n==1:
        if data[1] > w:
            print(0)
        else:
            print(data[0])
        exit()
        
    def calc_half(goods):
        l = len(goods)
        res = [[0,0]]
        for i in range(l):
            vi,wi = goods[i]
            for j in range(2**i):
                res.append([res[j][0]+vi, res[j][1]+wi])
        res.sort(key=lambda x: x[1])
        for i in range(l**2 - 1):
            if(res[i][0] > res[i+1][0]):
                res[i+1][0] = res[i][0]
        return res
    
    res1 = calc_half(vw[:n//2])
    res2 = calc_half(vw[n//2:])
    l1 = len(res1)
    l2 = len(res2)

    ans = 0
    j = l2-1
    for i in range(l1):
        while res1[i][1] + res2[j][1] > w:
            j -= 1
            if(j < 0):
                print(ans)
                exit()
        ans = max(ans,res1[i][0] + res2[j][0])
    print(ans)








