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

if n==2:
    print('dict')
    exit()

cnt = 0
for i in range(1,n-1):
    if s[i] == '{':
        cnt += 1
    elif s[i] == '}':
        cnt -= 1
    elif s[i] == ':' and cnt == 0:
        print('dict')
        exit()

print('set')