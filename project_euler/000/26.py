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
f = open('p018_triangle.txt', 'r')
sys.stdin = f

n = 1000
ans = [(1,3)]
for i in range(4,n):
    order = [-1] * i
    x = 1
    for j in range(1,n+10):
        x = (x*10)%i
        if(x==0):
            break
        if(order[x] != -1):
            cyc = j- order[x]
            ans.append((cyc,i))
            break
        order[x] = j

ans.sort(reverse=True)
print(ans[:10])



'''
普通に計算できそう

'''
