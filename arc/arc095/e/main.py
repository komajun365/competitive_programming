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

h,w = map(int,input().split())
s = [input() for _ in range(h)]

cnt = dict()
for si in s:
    for sj in si:
        if sj in cnt:
            cnt[sj] += 1
        else:
            cnt[sj] = 1

odd = 0
min_s = ''
min_cnt = 200
for k,v in cnt.items():
    if v % 2 == 1:
        odd += 1
    if v < min_cnt:
        min_cnt = v
        min_s = k

if odd > h*w % 2:
    print('NO')
    exit()


