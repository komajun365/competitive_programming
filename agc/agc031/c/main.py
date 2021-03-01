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
sys.setrecursionlimit(10**9)

n,a,b = map(int,input().split())

def calc(l,x,y,mask):
    if l == 1:
        return [x,y]
    
    xor = x ^ y
    for p in range(n):
        if (mask >> p) & 1 and (xor >> p) & 1:
            mask2 = mask - (1<<p)
            break
    
    for i in range(n):
        if (mask2 >> i) & 1:
            x2 = x ^ (1<<i)
            y2 = x2 ^ (1<<p)
            if y2 != y:
                break
    
    res = calc(l-1,x,x2,mask2) + calc(l-1,y2,y,mask2)

    # print(l,x,x2,y2,y,mask,mask2)
    return res

cnt_a = sum([(a>>i) & 1 for i in range(n)])
cnt_b = sum([(b>>i) & 1 for i in range(n)])
if (cnt_a - cnt_b) % 2 == 0:
    print('NO')
    exit()

print('YES')

ans = calc(n,a,b,2**n-1)
print(' '.join(map(str,ans)))
