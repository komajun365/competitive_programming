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

h,w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]
b = [list(map(int,input().split())) for _ in range(h)]

ans = 0
for i in range(h-1):
    for j in range(w-1):
        dif = b[i][j] - a[i][j]
        ans += abs(dif)
        for i2,j2 in zip([0,0,1,1],[0,1,0,1]):
            i2 += i
            j2 += j
            a[i2][j2] += dif

for i in range(h):
    for j in range(w):
        if a[i][j] != b[i][j]:
            print('No')
            exit()

print('Yes')
print(ans)