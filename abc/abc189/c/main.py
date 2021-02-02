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

n = int(input())
a = list(map(int,input().split()))

ans = 0
for i in a:
    tmp = 0
    i_max = 0
    for j in range(n):
        if a[j] >= i:
            tmp += 1
        else:
            tmp = 0        
        i_max = max(tmp,i_max)
    ans = max(ans, i_max * i)

print(ans)
