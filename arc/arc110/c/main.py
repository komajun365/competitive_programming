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
p = list(map(int,input().split()))

move = 0
for i,pi in enumerate(p):
    pi -= 1
    move += abs(i-pi)

if move != (n-1) * 2:
    print(-1)
    exit()

links = [set() for _ in range(n-1)]
cnt = [0] * (n-1)
deg_in = [0] * (n-1)

for i,pi in enumerate(p):
    pi -= 1
    if pi < i:
        for j in range(pi,i):
            cnt[j] += 1
            if j != pi:
                links[j].add(j-1)
                deg_in[j-1] += 1
    elif i < pi:
        for j in range(i,pi):
            cnt[j] += 1
            if j != i:
                links[j-1].add(j)
                deg_in[j] += 1

if max(cnt) != 2 or min(cnt) != 2:
    print(-1)
    exit()

stack = []
for i in range(n-1):
    if deg_in[i] == 0:
        stack.append(i)

ans = []
while stack:
    i = stack.pop()
    ans.append(i+1)
    for j in links[i]:
        deg_in[j] -= 1
        if deg_in[j] == 0:
            stack.append(j)

if len(ans) != n-1:
    print(-1)
    exit()

print('\n'.join(map(str,ans)))


# print(links)

