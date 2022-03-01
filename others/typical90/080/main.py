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

n,d = map(int,input().split())
a = list(map(int,input().split()))

def count_bit(x):
    res = 0
    while x > 0:
        res += x&1
        x >>= 1
    return res

ans = 0
for bi in range(1<<n):
    cnt_bi = count_bit(bi)
    ones = 0
    for j in range(n):
        if (bi >> j) & 1:
            ones |= a[j]
    
    cnt_ones = count_bit(ones)
    if cnt_bi % 2 == 0:
        ans += 1 << (d-cnt_ones)
    else:
        ans -= 1 << (d-cnt_ones) 
print(ans)