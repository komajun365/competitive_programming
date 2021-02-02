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

'''
愚直に数えていく。
10**7 まで頑張るとして、
最大で10**21
同じ数字は高々21回しか出てこない
数字の出現回数の組み合わせは、20桁の数字で管理できる。
'''
from collections import defaultdict
d = defaultdict(int)
cnt = defaultdict(int)

plus = {}
for i in range(10):
    plus[i] = 10**(i*2)

for i in range(10**5):
    num = i**3
    key = 0
    while(num>0):
        key += plus[num%10]
        num = num//10
    if(d[key] == 0):
        d[key] = i**3
    cnt[key] += 1
    if(cnt[key]==5):
        print(d[key])
        exit()
