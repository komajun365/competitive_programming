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

n,a,b = map(int,input().split())

def calc(n,a,b):
    if(n > a*b)|(a+b > n+1):
        return
        # print(-1)
        # exit()
    if(a==1)|(b==1):
        if(b==n):
            ans = list(range(n,-1,-1))
            print(' '.join(map(str,ans)))
        elif(a==n):
            ans = list(range(1,n+1))
            print(' '.join(map(str,ans)))
        else:
            print(-1)
        exit()

    ans = []
    top = n
    while(top > 0):
        if(top-a >= b):
            for i in range(top-a+1,top+1):
                ans.append(i)
            top -= a
            b -= 1
            continue
        a = top-b+1
        for i in range(top-a+1,top+1):
            ans.append(i)
        for i in range(b-1,0,-1):
            ans.append(i)
        break

    print(' '.join(map(str,ans)))
