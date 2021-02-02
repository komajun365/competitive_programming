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
a = list(map(lambda x: int(x)-1,input().split()))
ans = []
for i in range(n):
    x = i
    cnt = 0
    while(True):
        x = a[x]
        cnt += 1
        if(x == i):
            break
    ans.append(cnt)

print(' '.join(map(str,ans)))
