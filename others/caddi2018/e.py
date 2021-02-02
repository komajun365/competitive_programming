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

n = int(input())
a = list(map(int,input().split()))

if(n==1):
    print(0)
    exit()

all_plus = [0] * n
all_minus = [1] * n

for i in range(1,n):
    cnt = 0
    x = a[i]
    while(a[i-1] > x):
        cnt += 2
        x *= 4
    all_plus[i] = cnt + all_plus[i-1]

for i in range(n-2,-1,-1):
    cnt = 0
    x = a[i]
    while(x < a[i+1]):
        cnt += 2
        x *= 4
    all_minus[i] = cnt + all_minus[i+1]

cumsum_p = [0] * (n+1)
cumsum_m = [0] * (n+1)
for i in range(n):
    cumsum_p[n-1-i] = cumsum_p[n-i] + all_plus[n-1-i]
    cumsum_m[i+1] = cumsum_m[i] + all_minus[i]

print(all_plus)
print(all_minus)
print(cumsum_p)
print(cumsum_m)

ans = min(cumsum_p[0], cumsum_m[-1])
for i in range(1,n):
    #minusの数がi個あるとする。
    tmp = cumsum_m[i] - (all_minus[i-1]//2)*2*i
    tmp += cumsum_p[i] - (all_plus[i]//2)*2*(n-i)
    print(i,tmp)
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
