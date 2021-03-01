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

h,w,n,*xy = map(int,read().split())
blocks = [[h] for _ in range(w)]

it = iter(xy)
for x,y in zip(it,it):
    x -= 1
    y -= 1
    blocks[y].append(x)

for i in range(w):
    blocks[i].sort()

# print(blocks)

now = 0
ans = h
for i in range(w):
    stop = bisect.bisect_left(blocks[i],now)
    stop = blocks[i][stop]
    ans = min(ans,stop)
    
    now += 1
    if ans <= now or i+1 == w:
        print(ans)
        exit()

    idx = bisect.bisect_left(blocks[i+1],now)
    while(blocks[i+1][idx] == now):
        now += 1
        idx += 1
        if now == stop:
            print(ans)
            exit()
    # print(i,stop,now,ans)
        
print(ans)


# idx = 0
# if blocks[1][idx] == 0:
#     idx = 1
# while blocks[1][idx] == start+1:
#     idx += 1
#     now += 1
#     if now == w-1:
#         print(w)
#         exit()

# ans = w
# for i in range(h):
#     stop = bisect.bisect_left()




