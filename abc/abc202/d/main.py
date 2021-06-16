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

a,b,k = map(int,input().split())
n = a+b

com = [[0] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(n+1):
        if i < j:
            continue
        tmp = 1
        for x in range(i,i-j,-1):
            tmp *= x
        for y in range(1,j+1):
            tmp //= y
        com[i][j] = tmp

def calc(ai, bi, rem):
    if ai == 0:
        return 'b' * bi
    elif bi == 0:
        return 'a' * ai
    
    # a
    cnt_a = com[ai+bi-1][bi]
    if rem <= cnt_a:
        return 'a' + calc(ai-1, bi, rem)
    else:
        return 'b' + calc(ai, bi-1, rem-cnt_a)

ans = calc(a,b,k)
print(ans)