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
k = list(map(int,input().split()))

ans = [0] * n
ans[0] = k[0]
ans[-1] = k[-1]
for i in range(1,n):
    ans[i] = min(k[i-1:i+1])
print(' '.join(map(str,ans)))

'''
3 7 4



'''