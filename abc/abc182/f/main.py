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

# 再帰メモ化
import sys
sys.setrecursionlimit(10**6)
from functools import lru_cache

n,x = map(int,input().split())
a = list(map(int,input().split()))
x %= a[-1]
if(x == 0):
    print(1)
    exit()

@lru_cache(maxsize=10**9)
def calc(m):
    # print(m)
    l = 1
    if(m == a[-1]) or (m==0):
        return 1
    for i in range(n-2,0,-1):
        if( m % a[i] == 0):
            l = i+1
            break

    res = calc(m - m%a[l])
    res += calc(m - m%a[l] + a[l])
    # now = (m//a[l] +1) * a[l]
    # for i in range(l,n):
    #     second =  (m//a[i] +1) * a[i]
    #     if(now != second):
    #         res += calc(now)
    #         now = second
    # res += calc(now)
    
    # print(m)
    # print(cand)

    return res

ans = calc(x)
print(ans)






    
    





