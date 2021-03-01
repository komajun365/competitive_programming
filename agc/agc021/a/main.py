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

n = input()
l = len(n)
if l == 1:
    print(n)
    exit()

ans = int(n[0]) + 9 * (l-1)
if (int(n)+1) % (10**(l-1)) != 0:
    ans -= 1
print(ans)

