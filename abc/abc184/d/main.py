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

from functools import lru_cache

a,b,c = map(int,input().split())

@lru_cache(maxsize=10**5)
def calc(x,y,z):
    if(x==100) or (y==100) or (z==100):
        return 0
    res = calc(x+1,y,z)*x + calc(x,y+1,z)*y + calc(x,y,z+1)*z
    res /= (x+y+z)
    res += 1
    return res

ans = calc(a,b,c)
print(ans)