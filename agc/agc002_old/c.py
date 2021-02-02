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

n,l = map(int,input().split())
a = list(map(int,input().split()))

for i in range(n-1):
    if(a[i] + a[i+1]) >= l:
        print('Possible')
        ans = list(range(1,i+1)) + list(range(i+2,n))[::-1] + [i+1]
        print('\n'.join(map(str,ans)))
        exit()

print('Impossible')