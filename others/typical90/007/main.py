# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

import sys
read = sys.stdin.buffer.read
import bisect

n,*data = map(int,read().split())
a = data[:n]
q = data[n]
b = data[n+1:]

a.append(-1 * 10**10)
a.append(10**10)
a.sort()

ans = []
for bj in b:
    i = bisect.bisect_left(a, bj)
    ans.append( min(abs(bj-a[i-1]), abs(bj-a[i])) )

print('\n'.join(map(str,ans)))
