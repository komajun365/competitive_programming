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

stack = []
ans = []
cnt = 0
for ai in a:
    cnt += 1
    if len(stack) == 0:
        stack.append([ai,1])
    elif stack[-1][0] == ai:
        stack[-1][1] += 1
    else:
        stack.append([ai,1])
    
    while stack:
        if stack[-1][0] != stack[-1][1]:
            break
        cnt -= stack[-1][0]
        stack.pop()
    ans.append(cnt)

print(*ans, sep='\n')