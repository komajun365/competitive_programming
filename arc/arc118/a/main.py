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

t,n = map(int,input().split())

nums = [0] * (100+t+1)
for i in range(1,101):
    nums[i*(100+t)//100] = 1

cand = []
for i in range(1,100+t+1):
    if nums[i] == 0:
        cand.append(i)

l = len(cand)

n -= 1
ans = (n//l) * (100+t) + cand[n%l]
print(ans)