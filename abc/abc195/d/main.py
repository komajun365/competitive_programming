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

n,m,q,*data = map(int,read().split())
wv0 = data[:2*n]
it = iter(wv0)
wv = []
for w,v in zip(it,it):
    wv.append([w,v])
wv.sort(key = lambda x: x[1] * -1)
x = data[2*n:2*n+m]
query = data[2*n+m:]


def solve(l,r):
    box = x[:l-1] + x[r:]
    box.sort()
    l = len(box)

    res = 0
    for w,v in wv:
        for j in range(l):
            if box[j] >= w:
                res += v
                box[j] = 0
                break
    return res

it = iter(query)
for l,r in zip(it,it):
    print(solve(l,r))
