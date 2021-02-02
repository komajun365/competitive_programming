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

n,m = map(int,input().split())
if(n==1) and (m==0):
    print('1 2')
    exit()
if(m < 0) or (n-m <= 1):
    print(-1)
    exit()

if(m==0):
    ans = []
    for i in range(n):
        ans.append([1+i*2,2+i*2])
else:
    ans = []
    x = 2
    for i in range(m+1):
        ans.append([x,x+1])
        x += 2
    ans.append([1,x])
    x += 2

    rem = n-m-2
    for i in range(rem):
        ans.append([x,x+1])
        x += 2

print('\n'.join(map(lambda x: ' '.join(map(str,x)),ans)))
