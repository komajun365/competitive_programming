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

b0 = [0]
c0 = [a[0]]
for i in range(1,n):
    dif = a[i] - a[i-1]
    if dif > 0:
        b0.append(b0[-1] - dif)
        c0.append(c0[-1])
    elif dif < 0:
        b0.append(b0[-1])
        c0.append(c0[-1] + dif)
    else:
        b0.append(b0[-1])
        c0.append(c0[-1])

bc = b0 + c0
bc.sort()

bi = bc[n]
ci = a[0] - bi
ans = abs(bi) + abs(ci)
for i in range(1,n):
    dif = a[i] - a[i-1]
    if dif > 0:
        bi += dif
    elif dif < 0:
        ci += dif
    ans += abs(bi) + abs(ci)
    # print(ans)
print(ans)

# print(b0)
# print(c0)
# print(bc)
# print(bc[n])










