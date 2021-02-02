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

n,k = map(int,input().split())
s = input()

cnt = [0]
now = '1'
for i in range(n):
    if(s[i]==now):
        cnt[-1] += 1
    else:
        now = s[i]
        cnt.append(1)
cnt = cnt + [0,0]

m = len(cnt)
if( m <= 2*k+1):
    print(n)
    exit()

l = 0
r = 2*k+1
tmp = sum(cnt[:r])
ans = tmp
while(r+2 <= m):
    tmp += cnt[r] + cnt[r+1] - cnt[l] - cnt[l+1]
    ans = max(ans,tmp)
    l += 2
    r += 2
print(ans)

# print(cnt)

'''
a,b,c,d,e,f,...
'''
