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

k = int(input())
s = input()

n = len(s)
lens = [n]
for _ in range(k):
    x = lens[-1]
    if x == 0:
        print('impossible')
        exit()
    lens.append(x//2)

if lens[-1] == 1:
    print('impossible')
    exit()

group = [-1] * n
use = 0
for i in range(lens[-1]):
    group[i] = i
    use += 1
for i in range(len(lens)-1,0,-1):
    x = lens[i]
    r = lens[i-1]
    if x*2 != r:
        group[x] = use
        use += 1
    for j in range(x):
        group[r-j-1] = group[j]
    
cnt = [dict() for _ in range(use)]
for i in range(n):
    si = ord(s[i])
    if si in cnt[group[i]]:
        cnt[group[i]][si] += 1
    else:
        cnt[group[i]][si] = 1

tot = [0] * use
m1 = [[0,0] for _ in range(use)]
m2 = [[0,0] for _ in range(use)]

for i in range(use):
    ci = cnt[i]
    for key,val in ci.items():
        tot[i] += val
        if m1[i][0] < val:
            m2[i] = m1[i][::]
            m1[i] = [val,key]
        elif m2[i][0] < val:
            m2[i] = [val,key]

ans = 0
for i in range(use):
    ans += tot[i] - m1[i][0]

if lens[-1] != 0:
    level0 = []
    for i in range(lens[-1]):
        level0.append(m1[i][1])
    
    if level0 == level0[::-1]:
        dif = 10**6
        for i in range(lens[-1]):
            if i*2+1 == lens[-1]:
                continue
            dif = min(dif, m1[i][0] - m2[i][0])
        ans += dif
print(ans)



