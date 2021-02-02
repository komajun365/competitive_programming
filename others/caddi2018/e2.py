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

from collections import deque

n = int(input())
a = list(map(int,input().split()))

# import random
# n = 7
# a = [random.randint(1, 100) for i in range(n)]

if(n==1):
    print(0)
    exit()

all_plus = [0] * n
all_minus = [0] * n

for i in range(1,n):
    cnt = 0
    if( a[i-1] <= a[i]):
        x = a[i-1] * 4
        while(x <= a[i]):
            x *= 4
            cnt -= 2
    else:
        x = a[i]
        while(a[i-1] > x):
            cnt += 2
            x *= 4
    all_plus[i-1] = cnt

for i in range(n-2,-1,-1):
    cnt = 0
    if( a[i] >= a[i+1]):
        x = a[i+1]*4
        while(a[i] >= x):
            x *= 4
            cnt -= 2
    else:
        x = a[i]
        while(x < a[i+1]):
            cnt += 2
            x *= 4
    all_minus[i] = cnt

cumsum_p = [0] * (n+1)
d = deque()
for i in range(n-2,-1,-1):
    cumsum_p[i] = cumsum_p[i+1]
    if(all_plus[i] < 0):
        d.appendleft((i,all_plus[i]))
    elif(all_plus[i] > 0):
        cnt = all_plus[i]
        while(d):
            j,num_j = d.popleft()
            cumsum_p[i] += cnt * (j-i)
            if(num_j + cnt < 0):
                d.appendleft((j,num_j+cnt))
                cnt = 0
                break
            else:
                cnt = num_j + cnt
        cumsum_p[i] += cnt * (n-1-i)

cumsum_m = [1] * (n)
d = deque()
for i in range(n-1):
    cumsum_m[i+1] = cumsum_m[i] + 1
    if(all_minus[i] < 0):
        d.appendleft((i,all_minus[i]))
    elif(all_minus[i] > 0):
        cnt = all_minus[i]
        while(d):
            j,num_j = d.popleft()
            cumsum_m[i+1] += cnt * (i-j)
            if(num_j + cnt < 0):
                d.appendleft((j,num_j+cnt))
                cnt = 0
                break
            else:
                cnt = num_j + cnt
        cumsum_m[i+1] += cnt * (i+1)
cumsum_m = [0] + cumsum_m


# print(a)
# print(all_plus)
# print(all_minus)
# print(cumsum_p)
# print(cumsum_m)

ans = min(cumsum_p[0], cumsum_m[-1])
for i in range(1,n):
    #minusの数がi個あるとする。
    tmp = cumsum_m[i] + cumsum_p[i]
    ans = min(ans,tmp)

print(ans)


'''
並びあったAiとAjについて、それぞれの操作回数をxi,xjとする。
・Ai<Ajのとき
　－Xiが奇数でxjが偶数
　－xi,xjともに偶数で、


すべてのiへの操作回数が2回以上
→　全部からマイナス2回できる

というわけで、もっとも操作回数が少ないやつは1回以下。

全部1回以上。
操作後の値が最も0に近い数字の操作回数を０にすることができる。
（0の周囲を反復横跳びするだけで、他のものとの順序は入れ替わらない。）


全て正にする場合
全て負にする場合
で、それぞれ操作回数を求める。
あとは、どこで正負の反転をするか、で決められる。

'''
