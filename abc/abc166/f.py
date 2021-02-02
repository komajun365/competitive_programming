# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline

n,a,b,c = map(int,input().split())
ans = []
abc = [a,b,c]

d = {'AB\n':(0,1),'AC\n':(0,2),'BC\n':(1,2)}

if(a+b+c==0):
    print('No')
    exit()

if(a+b+c >= 3)|(a+b+c==1):
    for _ in range(n):
        s = input()
        x,y = d[s]
        if(abc[x]==0)&(abc[y]==0):
            print('No')
            exit()
        if(abc[x] < abc[y]):
            x,y = y,x
        abc[x] -= 1
        abc[y] += 1
        ans.append(y)

elif(a+b+c==2):
    ss = [input() for _ in range(n)]
    if(max(abc)==2):
        #(2,0,0)
        case = True
    else:
        case = False

    for i in range(n):
        s = ss[i]
        x,y = d[s]
        if(case)|(i==n-1):
            if(abc[x]==0)&(abc[y]==0):
                print('No')
                exit()
            if(abc[x] < abc[y]):
                x,y = y,x
            abc[x] -= 1
            abc[y] += 1
            case = False
        else:
            if(abc[x]!=abc[y]):
                if(abc[x] < abc[y]):
                    x,y = y,x
                abc[x] -= 1
                abc[y] += 1
                case = False
            else:
                sn = ss[i+1]
                if(x in d[sn]):
                    x,y = y,x
                abc[x] -= 1
                abc[y] += 1
                case = True
        ans.append(y)

print('Yes')
for i in ans:
    print(chr(i+ord('A')))
