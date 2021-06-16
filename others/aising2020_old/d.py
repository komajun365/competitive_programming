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
x = input()

memo = [-1] * (n+10)
def calc(x):
    if(memo[x] != -1):
        return memo[x]
    if(x==0):
        return 0
    cnt = 0
    x2 = x
    while(x2 > 0):
        cnt += (x2&1)
        x2 //= 2
    next = x%cnt
    memo[x] = 1 + calc(next)
    return memo[x]

cnt0 = x.count('1')
if(cnt0 == 0):
    ans = [1] * n
    print('\n'.join(map(str,ans)))
    exit()
if(cnt0==1):
    ans = [0] * n
    for i in range(n):
        ans1 = 1 + ( x[-1] == '1')
        if(x[i]=='0'):
            if(i==n-1):
                ans[i] = 2
            else:
                ans[i] = ans1
        else:
            ans[i] = 0
    print('\n'.join(map(str,ans)))
    exit()

rem_p = [0] * n
rem_m = [0] * n
rem_p[0] = 1
rem_m[0] = 1%(cnt0-1)

for i in range(1,n):
    rem_p[i] = (2*rem_p[i-1])%(cnt0+1)
    rem_m[i] = (2*rem_m[i-1])%(cnt0-1)

x_p = 0
x_m = 0
for i in range(n):
    if(x[n-1-i] == '1'):
        x_p += rem_p[i]
        x_m += rem_m[i]
x_p %= (cnt0+1)
x_m %= (cnt0-1)

ans = [0] * n
for i in range(n):
    if(x[i]=='1'):
        first = (x_m - rem_m[n-1-i])%(cnt0-1)
        ans[i] = calc(first) + 1
    else:
        first = (x_p + rem_p[n-1-i])%(cnt0+1)
        ans[i] = calc(first) + 1

print('\n'.join(map(str,ans)))
