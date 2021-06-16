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
a,b = map(int,input().split())

if n <= a or a > b:
    print('Takahashi')
elif b > a:
    print('Aoki')
else:
    if n % (a+1) == 0:
        print('Aoki')
    else:
        print('Takahashi')