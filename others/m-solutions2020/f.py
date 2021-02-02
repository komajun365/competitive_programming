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
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

n = int(readline())
xyu = read().split()

# x,y,/=p.\=m
num = 200_000
x,y,p,m = dict(),dict(),dict(),dict()
for i in [x,y]:
    for s in 'URDL':
        i[s] = [[] for _ in range(num+1)]

for i in [p,m]:
    for s in 'URDL':
        i[s] = [[] for _ in range(num*2+1)]

it = iter(xyu)
for a,b,c in zip(it,it,it):
    a = int(a)
    b = int(b)
    if(c in 'UD'):
        y[c][a].append(b)
    if(c in 'RL'):
        x[c][b].append(a)

    p[c][num + a-b].append(b)
    m[c][a+b].append(b)

inf = 10**10
ans = inf
for i in [x]:
    for j in range(num+1):
        #RL
        if(len(i['R'][j])>0)&(len(i['L'][j])>0):
            a = i['R'][j]
            a.sort()
            b = i['L'][j]
            b.sort()
            b_ind = 0
            for ai in a:
                while(b_ind < len(b)):
                    if( ai > b[b_ind]):
                        b_ind += 1
                    else:
                        break
                if(b_ind == len(b)):
                    break
                ans = min(ans, abs(ai-b[b_ind])*5)

for i in [y]:
    for j in range(num+1):
        #UD
        if(len(i['U'][j])>0)&(len(i['D'][j])>0):
            a = i['U'][j]
            a.sort()
            b = i['D'][j]
            b.sort()
            b_ind = 0
            for ai in a:
                while(b_ind < len(b)):
                    if( ai > b[b_ind]):
                        b_ind += 1
                    else:
                        break
                if(b_ind == len(b)):
                    break
                ans = min(ans, abs(ai-b[b_ind])*5)

for i in [p]:
    for j in range(num*2+1):
        #UL
        if(len(i['U'][j])>0)&(len(i['L'][j])>0):
            a = i['U'][j]
            a.sort()
            b = i['L'][j]
            b.sort()
            b_ind = 0
            for ai in a:
                while(b_ind < len(b)):
                    if( ai > b[b_ind]):
                        b_ind += 1
                    else:
                        break
                if(b_ind == len(b)):
                    break
                ans = min(ans, abs(ai-b[b_ind])*10)

        #RD
        if(len(i['R'][j])>0)&(len(i['D'][j])>0):
            a = i['R'][j]
            a.sort()
            b = i['D'][j]
            b.sort()
            b_ind = 0
            for ai in a:
                while(b_ind < len(b)):
                    if( ai > b[b_ind]):
                        b_ind += 1
                    else:
                        break
                if(b_ind == len(b)):
                    break
                ans = min(ans, abs(ai-b[b_ind])*10)

for i in [m]:
    for j in range(num*2+1):
        #UR
        if(len(i['U'][j])>0)&(len(i['R'][j])>0):
            a = i['U'][j]
            a.sort()
            b = i['R'][j]
            b.sort()
            b_ind = 0
            for ai in a:
                while(b_ind < len(b)):
                    if( ai > b[b_ind]):
                        b_ind += 1
                    else:
                        break
                if(b_ind == len(b)):
                    break
                ans = min(ans, abs(ai-b[b_ind])*10)

        #LD
        if(len(i['L'][j])>0)&(len(i['D'][j])>0):
            a = i['L'][j]
            a.sort()
            b = i['D'][j]
            b.sort()
            b_ind = 0
            for ai in a:
                while(b_ind < len(b)):
                    if( ai > b[b_ind]):
                        b_ind += 1
                    else:
                        break
                if(b_ind == len(b)):
                    break
                ans = min(ans, abs(ai-b[b_ind])*10)

if(ans==inf):
    print('SAFE')
else:
    print(ans)
