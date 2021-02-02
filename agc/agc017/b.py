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

n,a,b,c,d = map(int,input().split())
n -= 1

target = b-a

for i in range(n+1):
    left = c*i - d*(n-i)
    right = d*i - c*(n-i)
    if(left <= target <= right):
        print('YES')
        exit()

print('NO')

'''
n回のうち、
プラスにi回
マイナスにn-i回動くとする。
すると、プラス側はci~di
マイナス側は-d(n-i)~-c(n-i)なので

取りうる移動範囲は
ci-d(n-i) ~ di-c(n-i)

500000だし、全部計算すればよいですね


'''
