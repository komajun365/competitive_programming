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

p = int(input())
if p == 1:
    print(1)
    exit()

f1,f2 = 1,1
for i in range(3,10**5):
    f1,f2 = f2, f1+f2
    if f2 % p == 0:
        print(i)
        exit()

print(-1)

