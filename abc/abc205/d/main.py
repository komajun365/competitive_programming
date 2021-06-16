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


import sys
read = sys.stdin.buffer.read
import bisect

n,q,*data = map(int,read().split())
a = data[:n]
k = data[n:]

def get_num(x):
    num = bisect.bisect_left(a, x)
    res = x - num
    if num < n:
        if a[num] == x:
            res -= 1
    return res

# x >= k
def get_k(ki):
    ng = 0
    ok = 10**18 + 10**6
    while ok - ng > 1:
        mid = (ok+ng)//2
        if get_num(mid) >= ki:
            ok = mid
        else:
            ng = mid
    return ok

ans = []
for i in range(q):
    ans.append(get_k(k[i]))

print('\n'.join(map(str,ans)))


# for i in range(1,10):
#     print(get_num(i))

'''
1,2,5,7

5 = 5 - 2 = 3
6 = 6 - 3 = 3
'''