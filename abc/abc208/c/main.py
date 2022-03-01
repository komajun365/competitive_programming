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
a = list(map(int,input().split()))

a2 = [(ai<<20) + i for i,ai in enumerate(a)]
a2.sort()

ans = [k//n] * n
for i in range(k % n):
    ans[a2[i] % (1<<20)] += 1
print('\n'.join(map(str,ans)))