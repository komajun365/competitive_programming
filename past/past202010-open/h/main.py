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

import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

n,m,k = map(int,readline().split())
s = read().split()

l = min(n,m)
cnt_max = [0] * (m+1)

for num in range(10):
    ns = str(num)
    cumsum = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if(s[i][j] == ns):
                cumsum[i][j] += 1
    for i in range(n):
        for j in range(1,m):
            cumsum[i][j] += cumsum[i][j-1]
    for i in range(1,n):
        for j in range(m):
            cumsum[i][j] += cumsum[i-1][j]
    
    for w in range(1,l+1):
        for i in range(n-w+1):
            for j in range(m-w+1):
                tmp = (cumsum[i+w-1][j+w-1] - cumsum[i+w-1][j-1] 
                        - cumsum[i-1][j+w-1] + cumsum[i-1][j-1])
                cnt_max[w] = max(cnt_max[w], tmp)

ans = 1
for w in range(1,l+1):
    if(cnt_max[w] + k >= w**2):
        ans = w
print(ans)




'''
0-9まで2次元imosをする
→　10 * NM
1*1 ~ n*n まで、最大値を数える
→　10 * NNM
'''