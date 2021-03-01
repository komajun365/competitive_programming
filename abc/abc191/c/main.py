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

ans = 0
for i in range(h-1):
    for j in range(w-1):
        cnt = 0
        for x in [0,1]:
            for y in [0,1]:
                if s[i+x][j+y] == '.':
                    cnt += 1
        if cnt % 2 == 1:
            ans += 1
print(ans)