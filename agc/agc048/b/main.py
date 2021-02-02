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
b = list(map(int,input().split()))
ans = sum(a)
dif = [bi-ai for ai,bi in zip(a,b)]
d1 = dif[::2]
d1.sort(reverse=True)
d2 = dif[1::2]
d2.sort(reverse=True)

for i in range(len(d1)):
    tmp = d1[i] + d2[i]
    if(tmp > 0):
        ans += tmp
    else:
        break
print(ans)