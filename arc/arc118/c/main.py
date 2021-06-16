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
if n == 3:
    print('6 10 15')
    exit()

nums = [0] * 10001
for x in [6,10,15]:
    for i in range(1,10000):
        if x*i > 10000:
            break
        nums[x*i] = 1

ans = []
cnt = 0
for i in range(10001):
    if nums[i] == 1:
        ans.append(i)
        cnt += 1
    if cnt == n:
        break
    
print(' '.join(map(str,ans)))