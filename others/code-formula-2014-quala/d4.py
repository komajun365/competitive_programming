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
k = input()

ss = set(s)
ks = set(k)

unknown = 36 - len(ks)
will_use = 0
for i in ss:
    if(not i in ks):
        will_use += 1
not_use = unknown - will_use

ans = len(s)
for i in range(will_use):
    ans += 2 * i/(i+1)

ans += 2 * not_use * will_use/(will_use+1)

print(ans)


'''
chokudai解説方針
https://www.slideshare.net/chokudai/code-formula2014-quala


'''
