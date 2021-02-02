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

n,m = map(int,input().split())
a = list(map(int,input().split())) + [0]
b = list(map(int,input().split())) + [0]
mod  = 10**9 + 7

a.sort(reverse=True)
b.sort(reverse=True)

ai,bi = 0,0
ans = 1
free = 0
for i in range(n*m,0,-1):
    if(a[ai] > i) or (b[bi] > i):
        print(0)
        exit()
    elif(a[ai] == b[bi] == i):
        ai += 1
        bi += 1
        free += ai + bi - 2
    elif(a[ai] == i):
        ai += 1
        free += bi-1
        ans *= (bi)
        ans %= mod
    elif(b[bi] == i):
        bi += 1
        free += ai-1
        ans *= (ai)
        ans %= mod
    else:
        if(free==0):
            print(0)
            exit()
        ans *= free
        ans %= mod
        free -= 1
    # print(i,ai,bi,free,ans)
print(ans)



