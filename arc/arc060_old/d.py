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
s = int(input())
if(n<s):
    print(-1)
    exit()
elif(n==s):
    print(n+1)
    exit()

lim = 10**6
for i in range(2,lim+1):
    tmp = 0
    x = n
    while(x > 0):
        tmp += x%i
        x //= i
    if(tmp==s):
        print(i)
        exit()

#2桁
ns = n-s
inf = 10**12
ans = inf
for i in range(1,ns+1):
    if(i**2 > ns):
        break

    if(ns%i==0):
        b = ns//i + 1
        y = n-(b*i)
        if(i+y==s)&(0<=y<b):
            ans = min(ans,b)

if(ans==inf):
    print(-1)
else:
    print(ans)



'''
sがでかいんじゃー

bが最小ということは、
b進数表記したときに桁が多い

桁数を決め打ちすると全探索できる？　→　できなさそう
・b==2の時
log(n,2)桁　→　maxで40桁ぐらい

桁数を決めていい感じの計算ができないか
・2桁
n = bx+y
s = x+y
n-s = (b-1)x  <- (x<b,y<b)

・3桁
n = b**2*x+by+z
s = x+y+z
n-s = (b**2-1)x + (b-1)y = (b-1)( (b+1)x + y)

b = 10**6ぐらいまでは愚直に計算する。
この後はどう考えても2桁以下になっているはず！
すると、n-s = (b-1)x  <- (x<b,y<b) <- ( x<=b-1 )なので
n-sの約数を求めて、一番小さいbをgetすればよさそう。

'''
