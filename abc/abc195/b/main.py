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

a,b,w = map(int,input().split())
w *= 1000

ans = [1000001, 0]
for i in range(10**6+1):
    ai = a * i
    bi = b * i
    if ai <= w <= bi:
        ans[0] = min(ans[0], i)
        ans[1] = max(ans[1], i)

if ans == [1000001, 0]:
    print('UNSATISFIABLE')
else:
    print(*ans)