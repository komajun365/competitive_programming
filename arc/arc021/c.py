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

k = int(readline())
n = int(readline())
ad = list(map(int,read().split()))

def calc(m):
    tot = 0
    cnt = 0
    for i in range(n):
        a,d = ad[i*2:i*2+2]
        cnt_i = (m-a)//d + 1
        if(cnt_i > 0):
            cnt += cnt_i
            tot += a * cnt_i + d * (cnt_i-1) * cnt_i//2

    return cnt,tot

if(calc(1)[0] >= k):
    print(k)
    exit()

ng = 1
while(True):
    cand = ng*2
    if(calc(cand)[0] >= k):
        ok = cand
        break
    ng = cand

while(ok-ng>1):
    mid = (ng+ok)//2
    if(calc(mid)[0] >= k):
        ok = mid
    else:
        ng = mid

cnt,tot = calc(ng)
ans = tot + (k-cnt)*ok
print(ans)
# print(cnt,tot)



'''
二分探索
'''
