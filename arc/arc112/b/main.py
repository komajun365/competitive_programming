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

b,c = map(int,input().split())

if b == 0:
    do2 = c //2
    over = max(0, do2 * 2 + (c % 2) - 1)
    ans = 1 + over

elif b > 0:
    do2 = c // 2
    if do2 >= b:
        under = b*2-1
    else:
        under = max(0, do2 * 2 + (c % 2) - 1)
    
    c -= 1
    do2 = c // 2
    over = max(0, do2 * 2 + (c % 2) -1)
    ans = 2 + under + over

else:
    do2 = c // 2
    over = max(0, do2 * 2 + (c % 2) -1)

    c -= 1
    b *= -1
    do2 = c // 2
    if do2 >= b:
        under = b*2-1
    else:
        under = max(0, do2 * 2 + (c % 2) -1)

    ans = 2 + under + over

print(ans)