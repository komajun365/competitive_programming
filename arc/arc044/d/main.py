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
a = [i-1 for i in list(map(int,input().split()))]

idx = [0] * n
for i,ai in enumerate(a):
    idx[ai] = i

idx.append(-1)

ans = [''] * n
ch = 0
back = -2
for ai in a:
    if idx[ai+1] < back:
        ch += 1
    
    if ch == 26:
        print(-1)
        exit()
    
    ans[ai] = chr(ch + ord('A'))
    back = idx[ai+1]

print(''.join(ans))

