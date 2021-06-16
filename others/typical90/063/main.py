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

h,w,*p = map(int,read().split())

ans = 0
for bi in range(1,1<<h):
    i_cand = []
    for i in range(h):
        if (bi >> i) & 1:
            i_cand.append(i)
    cnt = dict()
    max_cnt = 0
    for j in range(w):
        num = p[i_cand[0]*w + j]
        for i in i_cand[1:]:
            if p[i*w + j] != num:
                break
        else:
            cnt[num] = cnt.get(num,0) + 1
            max_cnt = max(max_cnt, cnt[num])
    
    ans = max(ans, len(i_cand) * max_cnt)
print(ans)

