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
if n == 1:
    print('Not Prime')
    exit()

if n < 4:
    print('Prime')
    exit()

for i in range(2,n):
    if i**2 > n:
        print('Prime')
        exit()
    if n % i == 0:
        break

if n % 10 in [1,3,7,9]:
    tot = 0
    while n > 0:
        tot += n%10
        n //= 10
    if tot % 3 != 0:
        print('Prime')
        exit()
print('Not Prime')