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

n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

def check(t):
    if(a[-1] >= t):
        return False
    rem = k
    free = 0
    for ai,bi in zip(a[::-1],b[::-1]):
        bi -= free
        if(bi <= 0):
            free = -bi
            continue
        num = -( -bi//(t-ai) )
        rem -= num
        if(rem < 0):
            return False
        free = num*(t-ai) - bi
    return True

ok = 10**20
ng = 0
while(ok-ng > 1):
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)





'''
総移動距離は少ないほうが良い
仕事量の合計
'''