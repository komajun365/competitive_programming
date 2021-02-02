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

s = [input() for _ in range(18)]

def check(x,y,z):
    x *= 2
    y *= 2
    z *= 2
    for i in range(1,7):
        cnt = -2
        cnt += (x >> i)&1
        cnt += (y >> i+1)&1
        cnt += (y >> i-1)&1
        cnt += (z >> i)&1
        if(((y >> i)&1)*2 -1)*cnt < 0:
            return 0
    return 1

ok = [[] for _ in range(2**6)]
for x in range(2**6):
    ok[x] = [[0] * (2**6) for _ in range(2**6)]
    for y in range(2**6):
        for z in range(2**6):
            ok[x][y][z] = check(x,y,z)

mask = [[0,0] for _ in range(18)]
for i,si in enumerate(s):
    for j,s_ij in enumerate(si):
        if(s_ij == '0'):
            mask[i][0] += 1<<j
        elif(s_ij == '1'):
            mask[i][1] += 1<<j

dp = [[0] * (2**6) for _ in range(2**6)]
for y in range(2**6):
    x = 0
    if( (y & mask[0][0]) != 0) or ((y & mask[0][1]) != mask[0][1]):
        continue
    for z in range(2**6):
        dp[y][z] = ok[x][y][z]

for i in range(1,18):
    next = [[0] * (2**6) for _ in range(2**6)]
    for y in range(2**6):
        if( (y & mask[i][0]) != 0) or ((y & mask[i][1]) != mask[i][1]):
            continue
        for x in range(2**6):
            for z in range(2**6):
                if(ok[x][y][z]):
                    next[y][z] += dp[x][y]
    dp,next = next,dp
    # print(sum(map(sum,dp)))

ans = 0
for x in range(2**6):
    ans += dp[x][0]
print(ans)

    




'''
0xxxxxx0
0yyyyyy0
0zzzzzz0

xxxxxxとzzzzzzが決まれば
yyyyyyの個数は数えられる？
2**18 * 5≒10**6のオーダーで前計算可能

xxxxxx
yyyyyy
から
zzzzzzのパターン数を数えられる？

'''