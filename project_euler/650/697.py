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
一様乱数をn回かけ合わせた後に、累積確率25%以下の値をxとして、
log10(1/x)をこたえてね、という問題。

log10(1/x) = -log10(x)


(0-1)^n
log ((0-1)^n) = Σ log(0-1)

n回かけた後、x(0<=p<=1)となっている確率.
(0-1)^n = x



'''
