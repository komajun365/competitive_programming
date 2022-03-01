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

l,r = map(int,input().split())
mod = 10**9 + 7

def count(x):
    res = 0
    for i in range(1,20):
        if x > 10**i:
            left = 10**(i-1)
            right = 10**i - 1
            res += i * (left+right) * (right-left+1) //2
            res %= mod
        else:
            left = 10**(i-1)
            right = min(x, 10**i-1)
            res += i * (left+right) * (right-left+1) //2
            if x == 10**i:
                res += (i+1) * x
            res %= mod
            break
    return res

ans = count(r) - count(l-1)
ans %= mod
print(ans)
