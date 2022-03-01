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

y = int(input())
m = int(input())
d = int(input())

def calc(y,m,d):
    if m <= 2:
        y -= 1
        m += 12
    res = 365*y + y//4 - y//100 + y//400 + (306*(m+1))//10 + d - 429
    return res

ans = calc(2014,5,17) - calc(y,m,d)
print(ans)