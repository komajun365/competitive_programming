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

n,k = map(int,input().split())
ans = 0
for x in range(2,n*2+1):
    y = x-k
    if(y < 2) or (y > 2*n):
        continue
    tmp_x = n - abs(x-(1+n))
    tmp_y = n - abs(y-(1+n))
    ans += tmp_x*tmp_y
print(ans)


