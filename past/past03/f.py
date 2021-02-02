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
a = [input() for _ in range(n)]

ans = [0] * (n)
for i in range(n//2):
    for s in a[i]:
        if(s in a[n-i-1]):
            ans[i] = s
            ans[n-i-1] = s
            break
    else:
        print(-1)
        exit()

if(n%2==1):
    ans[n//2] = a[n//2][0]

print(''.join(ans))
