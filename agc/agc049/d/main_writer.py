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

# 解説方針。戻すDP

import sys
readline = sys.stdin.buffer.readline

mod=10**9+7

n,m=map(int,readline().split())
orgm=m

dp=[0]*(m+1)
dp[0]=1

def add(w):
    assert w>0
    for i in range(m-w+1):
        dp[i+w]=(dp[i+w]+dp[i])%mod
    if w in items:
        items[w] += 1
    else:
        items[w] = 1

    
def erase(w):
    assert w>0
    for i in reversed(range(m-w+1)):
        dp[i+w]=(dp[i+w]-dp[i])%mod
    items[w] -= 1

def c2(w):
    return w*(w+1)//2

items = dict()

add(n)
ans=0
for i in range(n):
    m=orgm-c2(i)
    if m<0:
        break
    if i==0:
        for j in range(1,n):
            add(c2(j))
    else:
        add(c2(i))
        erase(c2(n-i))
    ans=(ans+dp[m])%mod
    print(i,ans)
    print(items)
    print(dp)

print(ans)


