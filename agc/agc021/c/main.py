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

n,m,a,b = map(int,input().split())

ans = [['.'] * m for _ in range(n)]

if n%2 == 1:
    for i in range(min(a,m//2)):
        ans[-1][i*2] = '<'
        ans[-1][i*2+1] = '>'
        a -= 1

if m%2 == 1:
    for i in range(min(b,n//2)):
        ans[i*2][-1] = '^'
        ans[i*2+1][-1] = 'v'
        b -= 1

sq = (n//2) * (m//2)

num = 0
while a > 1:
    if num >= sq:
        print('NO')
        exit()
    i = num // (m//2)
    j = num % (m//2)
    ans[i*2][j*2] = '<'
    ans[i*2][j*2+1] = '>'
    ans[i*2+1][j*2] = '<'
    ans[i*2+1][j*2+1] = '>'
    a -= 2
    num += 1

while b > 1:
    if num >= sq:
        print('NO')
        exit()
    i = num // (m//2)
    j = num % (m//2)
    ans[i*2][j*2] = '^'
    ans[i*2][j*2+1] = '^'
    ans[i*2+1][j*2] = 'v'
    ans[i*2+1][j*2+1] = 'v'
    b -= 2
    num += 1

if sq - num >= a+b:
    if a == 1:
        i = num // (m//2)
        j = num % (m//2)
        ans[i*2][j*2] = '<'
        ans[i*2][j*2+1] = '>'
        a -= 1
        num += 1
    if b == 1:
        i = num // (m//2)
        j = num % (m//2)
        ans[i*2][j*2] = '^'
        ans[i*2+1][j*2] = 'v'
        b -= 1
        num += 1
elif sq == num+1 and a+b == 2 and n%2==1 and m%2==1:
    ans[-3][-3] = '^'
    ans[-2][-3] = 'v'
    ans[-1][-3] = '<'
    ans[-1][-2] = '>'
    ans[-1][-1] = 'v'
    ans[-2][-1] = '^'
    ans[-3][-1] = '>'
    ans[-3][-2] = '<'
    ans[-2][-2] = '.'
else:
    print('NO')
    exit()

print('YES')
print('\n'.join(map( lambda x: ''.join(x), ans )))