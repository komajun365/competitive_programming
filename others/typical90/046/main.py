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
b = list(map(int,input().split()))
c = list(map(int,input().split()))

cnt_a = [0] * 46
cnt_b = [0] * 46
cnt_c = [0] * 46
for ai,bi,ci in zip(a,b,c):
    cnt_a[ai%46] += 1
    cnt_b[bi%46] += 1
    cnt_c[ci%46] += 1

ans = 0
for i in range(46):
    for j in range(46):
        k = (-i-j) % 46
        ans += cnt_a[i] * cnt_b[j] * cnt_c[k]
print(ans)
