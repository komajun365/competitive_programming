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

k =int(input())
ans = 0
for a in range(1,k+1):
    for b in range(a,k+1):
        ab = a*b
        if ab > k:
            break
        max_c = k//ab
        if max_c < b:
            break

        if a==b:
            ans += 1
            ans += 3 * (max_c - b)
        else:
            ans += 3
            ans += 6 * (max_c-b)
print(ans)

