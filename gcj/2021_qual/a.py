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
read = sys.stdin.buffer.read

t,*data = map(int,read().split())
def calc(n, l):
    res = 0
    for i in range(n-1):
        # print(l)
        for j in range(n):
            if l[j] == i+1:
                res += j+1
                l = l[:j][::-1] + l[j+1:]
                break
    return res

ans = [''] * t
idx = 0
for i in range(t):
    n = data[idx]
    l = data[idx+1:idx+1+n]
    idx += n+1
    res = calc(n,l)
    ans[i] = 'Case #{}: {}'.format(i+1,res)
print('\n'.join(ans))


