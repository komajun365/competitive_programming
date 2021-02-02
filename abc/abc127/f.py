# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

q = int(input())

import sys
input = sys.stdin.readline
# ヒープキュー（最小値・最大値の取得）
from heapq import heappop,heappush
left = []
right = []

lsum = 0
rsum = 0
q1_num = 0
b = 0
for _ in range(q):
    qs = tuple(map(int, input().split()))
    if(qs[0]==1):
        b += qs[2]
        if(q1_num == 0):
            heappush(left, qs[1] * -1)
            lsum += qs[1]
            q1_num += 1
            continue
        elif(q1_num%2==1):
            tmp = heappop(left) * -1
            lsum -= tmp

        else:
            tmp = heappop(right)
            rsum -= tmp
        less =  min(tmp, qs[1])
        more =  max(tmp, qs[1])
        heappush(left, less * -1)
        heappush(right, more)
        lsum += less
        rsum += more
        q1_num += 1

    else:
        num = rsum - lsum + b
        tmp = heappop(left) * -1
        if(q1_num%2==1):
            num += tmp
        heappush(left, tmp * -1)
        print(' '.join(map(str, [tmp, num])))
#
# a b c d e
# (c-a)+(c-b)+(d-c)+(e-c)=d+e-a-b
# =sum(abcde) - 2* sum(ab) - c
#
# a b c d e f
# (c-a)+(c-b)+(d-c)+(e-c)+(f-c)
# =d+e+f-a-b-c
# =sum(abcdef) - 2*sum(abc)
