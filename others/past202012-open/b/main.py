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
s = input()

ans = ''
for i in range(n):
    si = s[i]
    ans2 = ''
    for ai in ans:
        if ai != si:
            ans2 += ai
    ans2 += si
    ans,ans2 = ans2,ans
print(ans)

