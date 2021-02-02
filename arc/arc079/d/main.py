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

k = int(input())
n = 50
cnt = ((k-1)//n + 1)*n
tot = ((k-1)//n + 1)*n + (n-1)*n
ans = [tot//n] * n

d = cnt - k
for i in range(n):
    if(i < d):
        ans[i] += (d-1) - n
    else:
        ans[i] += d

print(n)
print(' '.join(map(str,ans)))

'''
5 5
6 3
4 4
5 2
3 3
4 1
2 2
3 0
1 1
'''