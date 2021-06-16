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

h,w,*a = map(int,read().split())

tot_h = [0] * h
tot_w = [0] * w
ans = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        a_tmp = a[i*w+j]
        ans[i][j] -= a_tmp
        tot_h[i] += a_tmp
        tot_w[j] += a_tmp

for i in range(h):
    for j in range(w):
        ans[i][j] += tot_h[i] + tot_w[j]

print('\n'.join(map(lambda x: ' '.join(map(str, x)), ans)))

