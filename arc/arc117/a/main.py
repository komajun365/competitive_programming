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

a,b = map(int,input().split())

pm = 1
if a == b:
    ans0 = list(range(1,a+1))
    ans = ans0 + [-1*i for i in ans0]
    print(' '.join(map(str,ans)))
    exit()

if a < b:
    a,b = b,a
    pm = -1
ans_p = list(range(1,a+1))
ans_m = list(range(-1,-b,-1))

ans = ans_p + ans_m
ans.append(-1 * sum(ans))
ans = [pm * i for i in ans]
print(' '.join(map(str,ans)))