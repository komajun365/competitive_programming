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

n,a,b,c,d = map(int,input().split())
s = input()
a,b,c,d = a-1,b-1,c-1,d-1

def move(a,s):
    ar = a
    while(ar<n-2):
        if(s[ar+2]=='.'):
            ar += 2
        elif(s[ar+1]=='.'):
            ar +=1
        else:
            break
    if(ar!=n-1):
        ar+=(s[ar+1]=='.')
    return ar

def pr_end(x):
    if(x):
        print('Yes')
    else:
        print('No')
    exit()

ar = move(a,s)
br = move(b,s)

if(c<d):
    if(c<=ar)&(d<=br):
        pr_end(1)
    else:
        pr_end(0)

for i in range(b-1,d):
    if(s[i:i+3] =='...'):
        if(c<=ar)&(d<=br):
            pr_end(1)
        else:
            pr_end(0)

pr_end(0)


'''
入れ替わりするには3マス必要
たどり着くには岩2マスあると無理

全探索でOK

'''
