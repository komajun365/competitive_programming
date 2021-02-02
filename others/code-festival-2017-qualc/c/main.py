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

s = input()
s_rev = s[::-1]
n = len(s)

ans = 0
i,j = 0,0
while(i<n) and (j<n):
    if(s[i] == s_rev[j]):
        i += 1
        j += 1
    elif(s[i] == 'x'):
        i += 1
    elif(s_rev[j] == 'x'):
        j += 1
        ans += 1
    else:
        print(-1)
        exit()
print(ans + n-j)
