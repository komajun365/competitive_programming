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

n,m,v,p = map(int,input().split())
a = list(map(int,input().split()))

a.sort(reverse=True)

higher = a[p-1]
for i in range(p,n):
    if(a[i] == a[i-1]):
        higher += a[i]
        continue

    if(a[p-1]- a[i] > m):
        print(i)
        exit()

    if(higher - a[i]*(i-p+1) > min(n-v,i-p+1)*m):
        print(i)
        exit()

    higher += a[i]

print(n)

'''
ジャッジ投票後に、自分よりスコアの高い問題がp-1問以下である状況を作れるか、という問題？

スコアを降順に並べて、
p番目と同じスコアのものまでは無条件でOK
p+1番目以降の場合、
A(p)...A(p+k-1)、A(x=p+k)としましょう。

前にいるk個の中でtop集団に入る必要があります。
投票について、投票されなかった問題をマイナスにする操作だと考えます。
一人の投票権がv　＝　投票されない問題がn-v個

A(p)...A(p+k-1)のうち、min（n-v,k）個の問題からスコアをマイナスすることが可能です。
A(x)と同じ値までマイナスできればいいので、
sum（A(p)...A(p+k-1)） - a(x)*k < min（n-v,k)*m かつ、A(p)<= a(x)+vならなんとかなります！

3,2,2,1,1,0

'''
