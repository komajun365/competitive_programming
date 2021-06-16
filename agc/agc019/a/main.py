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

q,h,s,d = map(int,input().split())
n = int(input())
q *= 4
h *= 2
one = min(q,h,s)
if 2*one <= d:
    ans = one*n
else:
    ans = d * (n//2) + one * (n%2)
print(ans)