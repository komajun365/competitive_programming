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

s = input()
n = len(s)

ret = [0] * (n+10)
combo = [0] * (n+10)
ans = 0
kab = 5
charge = 0
for i in range(n):
    kab += ret[i]
    combo[i] += combo[i-1]
    charge -= 1
    if charge > 0:
        continue

    if s[i] == 'N':
        if kab < 1:
            continue
        kab -= 1
        ret[i+7] += 1
        combo[i+2] += 1
        ans += 10 + combo[i]//10
    elif s[i] == 'C':
        if kab < 3:
            continue
        kab -= 3
        ret[i+9] += 3
        combo[i+4] += 1
        ans += 50 + (combo[i]//10) * 5
        charge = 3

print(ans)


