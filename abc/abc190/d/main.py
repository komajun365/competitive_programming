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
n2 = 2*n

ans = 0
for d in range(10**6 *2):
    if n2 % (d+1) != 0:
        continue
    xy = n2 // (d+1)
    x = xy - d
    if x > 0 and x %2 == 0:
        ans += 2
print(ans)



