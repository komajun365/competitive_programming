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

w,h,q,*data = map(int,read().split())

beam_x = [[] for _ in range(10**5)]
beam_y = [[] for _ in range(10**5)]

it = iter(data)
for t,d,x in zip(it,it,it):
    t -= 1
    x -= 1
    if d == 0:
        beam_x[t].append(x)
    else:
        beam_y[t].append(x)

ans = 0
inf = 10**6
cnt = [0] * (w+2)
cnt[w] = inf
cnt[w+1] = inf
for beam in beam_x:
    beam.sort()
    for i in beam:
        cnt[i] = cnt[i-1] + 1
    for i in beam[::-1]:
        cnt[i] = min(cnt[i], cnt[i+1]+1)

ans += min(cnt)
# print(cnt)

cnt = [0] * (h+2)
cnt[h] = inf
cnt[h+1] = inf
for beam in beam_y:
    beam.sort()
    for i in beam:
        cnt[i] = cnt[i-1] + 1
    for i in beam[::-1]:
        cnt[i] = min(cnt[i], cnt[i+1]+1)

ans += min(cnt)

if ans >= inf:
    print(-1)
else:
    print(ans)

# print(cnt)
# print(beam_x[:10])