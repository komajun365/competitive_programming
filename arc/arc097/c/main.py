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
k = int(input())

n = len(s)
subs = set()
for i in range(n):
    for j in range(i+1,min(n+1,i+6)):
        subs.add(s[i:j])

subs = list(subs)
subs.sort()
# print(subs)
print(subs[k-1])

