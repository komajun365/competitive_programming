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
p = list(map(int,input().split()))

lim = sum(p)
dp = 1

for pi in p:
    dp |= dp << pi

ans = 0
while dp > 0:
    if dp & 1:
        ans += 1
    dp >>= 1
print(ans)