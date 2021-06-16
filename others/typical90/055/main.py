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

n,p,q = map(int,input().split())
a = list(map(int,input().split()))

ans = 0
for x1 in range(n-4):
    m1 = a[x1] % p
    for x2 in range(x1+1,n-3):
        m2 = m1 * a[x2] % p
        for x3 in range(x2+1,n-2):
            m3 = m2 * a[x3] % p
            for x4 in range(x3+1,n-1):
                m4 = m3 * a[x4] % p
                for x5 in range(x4+1,n):
                    m5 = m4 * a[x5] % p
                    if m5 == q:
                        ans += 1
print(ans)
