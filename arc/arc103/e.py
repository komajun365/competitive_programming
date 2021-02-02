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

s = input()
if(s[0]=='0')|(s[-1]=='1'):
    print(-1)
    exit()

n = len(s)
size = []
for i in range(1,n//2):
    sl = s[i]
    sr = s[n-2-i]
    if(sl != sr):
        print(-1)
        exit()
    if(sl=='1'):
        size.append(i+1)

size.append(n-1)
ans = []
now = 1
for si in size:
    for j in range(now+1,si+2):
        ans.append(' '.join(map(str,[now,j])))
    now = si+1

print('\n'.join(ans))
