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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,x = map(int,readline().split())
w = list(map(int,read().split()))

if(n==1):
    ans = 1*(w[0]==x)
    print(ans)
    exit()

w1 = w[:n//2]
w2 = w[n//2:]

def make_group(wi):
    len_n = len(wi)
    res = [0]
    for i in range(len_n):
        res2 = res[::]
        for j in res2:
            res.append(j+wi[i])
    return res

g1 = make_group(w1)
g2 = make_group(w2)
g1.sort()
g2.sort(reverse=True)

ans = 0
i = 0
j = 0
while(i<len(g1))&(j<len(g2)):
    n1 = g1[i]
    cnt1 = 1
    i += 1
    while(i<len(g1)):
        if(n1==g1[i]):
            cnt1 += 1
            i += 1
        else:
            break

    n2 = x-n1
    if(n2 < 0):
        break
    cnt2 = 0
    while(j<len(g2)):
        if(n2 < g2[j]):
            j += 1
        elif(n2 == g2[j]):
            j += 1
            cnt2 += 1
        else:
            break
    ans += cnt1*cnt2

print(ans)
# print(g1)
# print(g2)
