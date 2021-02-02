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

def move(al,ar,s):
    while(al>1):
        if(s[al-2]=='.'):
            al -= 2
        elif(s[al-1]=='.'):
            al-=1
        else:
            break
    if(al!=0):
        al-=(s[al-1]=='.')
    while(ar<n-2):
        if(s[ar+2]=='.'):
            ar += 2
        elif(s[ar+1]=='.'):
            ar +=1
        else:
            break
    if(ar!=n-1):
        ar+=(s[ar+1]=='.')
    return al,ar

def pr_end(x):
    if(x):
        print('Yes')
    else:
        print('No')
    exit()

al,ar = move(a-1,a-1,s)
bl,br = move(b-1,b-1,s)

# print(al,ar,bl,br,c,d)

if(c<d):
    if(al<=c-1<=ar)&(bl<=d-1<=br):
        pr_end(1)
    else:
        pr_end(0)

if(al!=bl):
    pr_end(0)

for i in range(al,ar-1):
    if(s[i:i+3] =='...'):
        if(al<=c-1<=ar)&(bl<=d-1<=br):
            pr_end(1)
        else:
            pr_end(0)

pr_end(0)


'''
入れ替わりするには3マス必要
たどり着くには岩2マスあると無理

全探索でOK

'''
