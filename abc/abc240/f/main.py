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

t,*case = map(int,read().split())
idx = 0
ans = []
for _ in range(t):
    n,m = case[idx:idx+2]
    idx += 2
    xy = case[idx:idx+2*n]
    idx += 2*n

    res = xy[0]
    now_a = 0
    now_b = 0
    for i in range(n):
        xi,yi = xy[i*2:i*2+2]
        next_b = now_b + xi*yi
        now_b += xi
        if i != 0 and now_b >= 0 and next_b < 0:
            add = -(-now_b // abs(xi)) 
            mid_b = now_b + (add-1)*xi
            res = max(res, now_a + (now_b + mid_b) * add //2)
        now_a += (now_b + next_b) * yi //2
        now_b = next_b
        res = max(res, now_a)
        # print(now_a,now_b,res)
            
    ans.append(res)
print(*ans, sep='\n')

