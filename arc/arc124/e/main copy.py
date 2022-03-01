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

n = int(input())
a = list(map(int,input().split()))
mod = 998244353

inv2 = pow(2, mod-2, mod)
inv6 = pow(6, mod-2, mod)

def com(n,k):
    if k == 1:
        return n % mod
    elif k == 2:
        return (n * (n-1) % mod) * inv2 % mod
    else:
        return ((n * (n-1) % mod) * (n-2) % mod) * inv6 % mod

ans = 0
# 1番目の人がN番目からもらったボールを選ばない
# dp0[0] := i+1番目の人がi番目からもらったボールを選ぶ
# dp0[1] := i+1番目の人がi番目からもらったボールを選ばない
# dp1 := 1回でもボールを渡さなかった人が出現した
dp0 = [0,0]
dp1 = [0,0]
dp1[0] = 0
dp1[1] = a[0]
dp0[0] = com(a[0]+1, 3) - dp1[0]
dp0[1] = com(a[0]+1, 2) - dp1[1]
print(dp0,dp1)
for i in range(1,n):
    dp01 = [0,0]
    dp11 = [0,0]
    dp11[0] += dp1[0] * com(a[i]+1, 2)
    dp11[0] += dp1[1] * com(a[i]+1, 3)
    dp11[0] %= mod
    dp11[1] += dp1[0] * com(a[i]+1, 1)
    dp11[1] += dp1[1] * com(a[i]+1, 2)
    dp11[1] %= mod

    print(dp01,dp11)

    move0 = dp0[0] 
    move1 = dp0[1] * a[i] % mod
    dp11[1] += move0 + move1
    dp11[1] %= mod

    print(dp01,dp11)

    dp01[0] += dp0[0] * com(a[i]+1, 2)
    dp01[0] += dp0[1] * com(a[i]+1, 3) - move0
    dp01[0] %= mod
    dp01[1] += dp0[0] * com(a[i]+1, 1)
    dp01[1] += dp0[1] * com(a[i]+1, 2) - move1
    dp01[1] %= mod

    dp0,dp01 = dp01,dp0
    dp1,dp11 = dp11,dp1
    print(dp0,dp1)
ans += dp1[1]

# 1番目の人がN番目からもらったボールを選ぶ
dp0 = [0,0]
dp1 = [0,0]
dp1[0] = 0
dp1[1] = 1
dp0[0] = com(a[0]+1, 2) - dp1[0]
dp0[1] = com(a[0]+1, 1) - dp1[1]
print('second')
print(dp0,dp1)
for i in range(1,n):
    dp01 = [0,0]
    dp11 = [0,0]
    dp11[0] += dp1[0] * com(a[i]+1, 2)
    dp11[0] += dp1[1] * com(a[i]+1, 3)
    dp11[0] %= mod
    dp11[1] += dp1[0] * com(a[i]+1, 1)
    dp11[1] += dp1[1] * com(a[i]+1, 2)
    dp11[1] %= mod

    move0 = dp0[0] 
    move1 = dp0[1] * a[i] % mod
    dp11[1] += move0 + move1
    dp11[1] %= mod

    dp01[0] += dp0[0] * com(a[i]+1, 2)
    dp01[0] += dp0[1] * com(a[i]+1, 3) - move0
    dp01[0] %= mod
    dp01[1] += dp0[0] * com(a[i]+1, 1)
    dp01[1] += dp0[1] * com(a[i]+1, 2) - move1
    dp01[1] %= mod

    dp0,dp01 = dp01,dp0
    dp1,dp11 = dp11,dp1
    print(dp0,dp1)
ans += dp1[0]

ans %= mod
print(ans)