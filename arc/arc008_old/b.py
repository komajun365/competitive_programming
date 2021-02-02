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

n,m = map(int,input().split())
name = input()
kit = input()

ans = 0
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for si in alp:
    n_cnt = name.count(si)
    k_cnt = kit.count(si)
    if(n_cnt>0)&(k_cnt==0):
        print(-1)
        exit()
    elif(n_cnt==0):
        continue
    ans = max(ans, -(-n_cnt//k_cnt))
print(ans)
