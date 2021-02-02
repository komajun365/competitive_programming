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

n,m = map(int,input().split())
s = []
for _ in range(n):
    s.append(input())

ans = [[0] * (m+2) for _ in range(n+2)]
for i in range(n):
    for j in range(m):
        if(s[i][j] == '#'):
            for i2 in [0,1,2]:
                i2 += i
                for j2 in [0,1,2]:
                    j2 += j
                    ans[i2][j2] += 1

for i in range(1,n+1):
    print(''.join(map(str,ans[i][1:-1])))

