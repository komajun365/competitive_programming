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

import itertools

n,m,k = map(int,input().split())
if(m==0):
    print(1)
    exit()
ab = [list(map(int,input().split())) for _ in range(m)]
ab_dict = dict()
for i,[a,b] in enumerate(ab):
    ab_dict[a*n + b] = i
    ab_dict[b*n + a] = i

bit_n = 2**m
move = [[0] * bit_n for _ in range(bit_n)]

for p in itertools.permutations(range(1,n),n-1):
    p2 = [0]
    p2 += list(p)
    bit_p = 0
    for i in range(-1,n-1):
        num = p2[i]*n + p2[i+1]
        if(num in ab_dict):
            bit_p += 1<<(ab_dict[num])

    for q in itertools.permutations(range(n),2):
        bit_q = bit_p
        for i,j in zip([q[0],q[0],q[1],q[1]],[q[0]+1,q[0]-1,q[1]+1,q[1]-1]):
            num = p2[i%n]*n + p2[j%n]
            if(num in ab_dict):
                if(bit_q >> ab_dict[num])&1:
                    bit_q -= (1<<(ab_dict[num]))

        for i,j in zip([q[0],q[0],q[1],q[1]],[q[1]+1,q[1]-1,q[0]+1,q[0]-1]):
            if((i%n)==(j%n)):
                i,j = q[0],q[1]
            num = p2[i%n]*n + p2[j%n]
            if(num in ab_dict):
                bit_q = (bit_q | (1 << ab_dict[num]))

        move[bit_p][bit_q] += 1
        # print(bit_p,bit_q)
        # print(p2)
        # print(q)

for i in range(bit_n):
    tot = sum(move[i])
    if(tot==0):
        continue
    for j in range((bit_n)):
        move[i][j] /= tot

def calc(x,move):
    len_x = len(x)
    res = [0] * len_x
    for i in range(len_x):
        for j in range(len_x):
            res[j] += x[i] * move[i][j]
    return res

start = 0
for i in range(n):
    num = i*n + (i+1)%n
    if(num in ab_dict):
        start += (1<<ab_dict[num])

x = [0] * bit_n
x[start] = 1

for _ in range(k):
    x = calc(x,move)

print(x[0])

# print(move)




'''
全探索間に合ってしまう？
間に合わないよやばいよ
n<=3の時はどうやっても無理

a,bが隣り合ってはいけない組み合わせの時、
・a,bが隣り合ってない　→　シャッフル後隣り合う
aのサイド二人とb、もしくはbのサイド二人とa、をシャッフルするパターン
4パターン

・a,bが隣り合ってない　→　シャッフル後隣り合わない
上記以外なのでn(n-1)//2 - 4

・a,bが隣り合っている　→　シャッフル後隣り合う
下記以外なのでn(n-1)//2 - 3

・a,bが隣り合っている　→　シャッフル後隣り合わない
aとb、aとbのサイド、bとaのサイド、nの3パターン

＝＝＝＝＝＝＝＝＝＝＝＝＝

最後の並びのパターンを決めておいて、
そこに到達できる可能性を数えるのは？

10! = 3628800 = 3.6*10**6
いけるかも。

所望の並びを与えられたときに、
dp[k][i][j] := 初期状態ではk人が所望の状態にあったとき、i回シャッフルをして、j人が所望の並びになっている確率

・OKの二人をpickしてしまう
if(j>=2):
    dp[k][i+1][j-2] += dp[k][i][j] * j*(j-1)/2
・OK,NGからひとりづつpick
if(j>=1):
    dp[k][i+1][j-1] += dp[k][i][j] * j*(n-j)
・NGから二人pickして、一人もOKにならない
if(n-j>=2):
    dp[k][i+1][j] += dp[k][i][j] * (n-j)*
    あ、だめだこれ。。事前の並びによって確率変わるわ。


'''

'''
完全グラフKnがあり、
全ての頂点を取って戻ってくる経路が与えられている。
頂点を二つx,y選び、
(lx,x),(x,rx)(ly,y),(y,ry)のパスを
(lx,y),(y,rx)(ly,x),(x,ry)に張り替える操作をk回する。

最終的に、m個の使いたくないパスを用いない経路になっている確率は？

Mの使われている組2**mから、
シャッフル後にそれぞれに遷移する確率を求めればいいのでは？

初期状態10!に55通り全探索すればいい？

'''


hoge = 1
for i in range(1,12):
    hoge *= i
    print(hoge)
