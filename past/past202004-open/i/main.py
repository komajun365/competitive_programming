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

ans = [n] * (2**n)
rem = list(range(2**n))
for i in range(1,n+1):
    next = []
    it = iter(rem)
    for x,y in zip(it,it):
        if(a[x] > a[y]):
            next.append(x)
            ans[y] = i
        else:
            next.append(y)
            ans[x] = i
    next,rem = rem,next

print('\n'.join(map(str,ans)))