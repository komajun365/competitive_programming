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

n,k = map(int,input().split())

if k <= n:
    ans = k**3
elif k <= 2*n:
    ans = k**3 - (k-n)**3 * 3
elif k <= 3*n:
    ans = n**3 * 6 - (3*n-k)**3
else:
    ans = n**3 * 6
print(ans)

'''
27 * 6 = 162

27 + 27 + 108

4*4*4 - 1*1*1*3


'''