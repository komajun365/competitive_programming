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

n,d,k,*data = map(int,read().split())
lr = data[:d*2]
st = data[d*2:]

ans = []
it = iter(st)
for s,t in zip(it,it):
    left = s
    right = s
    for i in range(n):
        l,r = lr[i*2:i*2+2]
        if l <= left <= r:
            left = l
        if l <= right <= r:
            right = r
        
        if left <= t <= right:
            ans.append(str(i+1))
            break

print('\n'.join(ans))

        
