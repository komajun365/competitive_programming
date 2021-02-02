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

def calc_un(x):
    res = 1
    for i in range(1,11):
        res += (1-2*(i%2))*(x**i)
    return res

def add_next(x):
    if(len(set(x))==1):
        res = x[::]
        res.append(x[0])
        return res

    dif = []
    for i in range(len(x)-1):
        dif.append(x[i+1]-x[i])

    dif_next = add_next(dif)
    res = x[::]
    res.append(x[-1] + dif_next[-1])
    return res

un = []
for i in range(1,20):
    un.append(calc_un(i))

print(un)
# print(add_next(un[:2]))

ans = 0
for i in range(1,11):
    un_i = un[:i]
    while(True):
        un_i = add_next(un_i)
        print(i,un_i)
        if( un[len(un_i)-1] != un_i[-1] ):
            ans += un_i[-1]
            break

print(ans)


'''
多項式にfitさせる？？？

差の差の差の・・・ってやっていくのかな？

'''
