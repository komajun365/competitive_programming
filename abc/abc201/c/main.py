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

ans = 0
for i in range(10000,20000):
    i = str(i)[1:]
    for j in range(10):
        if s[j] == 'o' and not str(j) in i:
            break
        elif s[j] == 'x' and str(j) in i:
            break
    else:
        ans += 1
print(ans)
