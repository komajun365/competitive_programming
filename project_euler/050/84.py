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

import numpy as np
import numpy.linalg as LA

di = 4
n = 40
prob = np.zeros((n,n))
# print(prob)

go = 0
jail = 10
g2j = 30
cc = [2,17,33]
ch = [7,22,36]
ch_next = [go,jail,11,24,39,5]
ch_next2 = [[15,15,12,4],[25,25,28,19],[5,5,12,33]]

for i in range(n):
    if(i==30):
        continue
    for j in range(2,di*2+1):
        prob[(i+j)%n][i] = (di - abs(di+1-j))/di**2

    for j in range(2,di*2+1,2):
        prob[(i+j)%n][i] -= 1/(di**4)
    prob[jail][i] += 1/(di**3)

    #g2j
    prob[jail][i] += prob[g2j][i]
    prob[g2j][i] = 0.0

    #cc
    for j in cc:
        prob[go][i] += prob[j][i]*1/16
        prob[jail][i] += prob[j][i]*1/16
        prob[j][i] *= 14/16

    #ch
    for ind,j in enumerate(ch):
        for k in ch_next:
            prob[k][i] += prob[j][i]*1/16
        for k in ch_next2[ind]:
            prob[k][i] += prob[j][i]*1/16
        prob[j][i] *= 6/16

prob = np.delete(prob,30,0)
prob = np.delete(prob,30,1)

# prob = prob.T
# for j,i in enumerate(prob):
#     print(j)
#     print(i)

# prob = prob.T
w,v = LA.eig(prob)
#
# print(w)

vec = []
for i,j in enumerate(w):
    if(abs(j-1) < 0.001):
        break

for j in v:
    vec.append(float(j[i]))

tot = sum(vec)
vec2 = []
for i in range(n-1):
    vec2.append((vec[i]/tot,i))

vec2.sort(reverse=True)
print(vec2)

'''
行列です。

何もなければ2~12マス先に進む。
ただし、2,4,6,8,10,12は3連続ぞろ目チャレンジの可能性があり、
それぞれ1/6**4　の確率でjailに行く。

CCに止まった場合、1/16でGOへ、1/16でJailへ飛ぶ。
Chanceに止まった場合もうまく処理する。

'''
