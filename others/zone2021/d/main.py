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

from collections import deque

s = input()
d = deque()

rev = 0
for si in s:
    if si == 'R':
        rev = 1-rev
        continue

    if rev == 0:
        d.append(si)
    else:
        d.appendleft(si)

def pop_():
    if rev == 1:
        return d.pop()
    else:
        return d.popleft()

ans = []
while d:
    x = pop_()
    if ans:
        if ans[-1] == x:
            ans.pop()
        else:
            ans.append(x)
    else:
        ans.append(x)

print(''.join(ans))