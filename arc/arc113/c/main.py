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
n = len(s)

base = ord('a')
idx = [[] for _ in range(26)]
for i,si in enumerate(s):
    idx[ord(si) - base].append(i)


right = [dict() for _ in range(26)]
for i in range(26):
    l = len(idx[i])
    for j in range(l-1):
        right[i][idx[i][j]] = idx[i][j+1]
    if l > 0:
        right[i][idx[i][l-1]] = n


ans = 0
last = [n,-1]
for i in range(n-2,-1,-1):
    if s[i] == s[i+1]:
        c = ord(s[i]) - base
        if last[1] == c:
            ans += last[0] - (i+1) + 1
        else:
            ans += n - (i+1) + 1

        while(idx[c]):
            if idx[c][-1] > last[0]:
                idx[c].pop()
                continue
            if idx[c][-1] >= i:
                idx[c].pop()
                ans -= 1
            else:
                break
        last = [i,c]

print(ans)

