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
music = []
for _ in range(n):
    title,time = input().split()
    music.append([title,int(time)])
x = input()

ans = 0
sleep = False
for title,time in music:
    if sleep:
        ans += time
    if title == x:
        sleep = True
print(ans)