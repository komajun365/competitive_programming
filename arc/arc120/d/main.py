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

base = (1<<20)-1
a_idx = [(ai << 20) + i for i,ai in enumerate(a)]
a_idx.sort()
idx = [0] * (2*n)
for i in range(n):
    idx[ a_idx[i] & base ] = 1

ans = []
cnt = 0
now = '()'
for i in range(2*n):
    if cnt == 0:
        if idx[i] == 0:
            now = '()'
        else:
            now = ')('
    ans.append(now[idx[i]])
    if ans[-1] == '(':
        cnt += 1
    else:
        cnt -= 1
print(''.join(ans))
    




    