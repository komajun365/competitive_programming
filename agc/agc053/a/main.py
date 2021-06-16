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
a = list(map(int,input().split()))

k = 10**4
for i in range(n):
    k = min(k, abs(a[i]-a[i+1]))

b = []
for i in range(k):
    tmp = [(ai+i)//k for ai in a]
    b.append(' '.join(map(str,tmp)))
print(k)
print('\n'.join(b))
