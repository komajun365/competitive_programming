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
s = [int(i) for i in input()]
t = [int(i) for i in input()]

s_idx = []
t_idx = []
for i in range(n-1,-1,-1):
    if s[i] == 1:
        s_idx.append(i)
    if t[i] == 1:
        t_idx.append(i)

ans = 0
while s_idx and t_idx:
    # print(s_idx, t_idx)
    si = s_idx.pop()
    ti = t_idx.pop()
    if si == ti:
        continue
    if si < ti:
        if not s_idx:
            print(-1)
            exit()
        sj = s_idx.pop()
        ans += sj-si
        t_idx.append(ti)
    elif ti < si:
        ans += si-ti

while s_idx:
    if len(s_idx) == 1:
        print(-1)
        exit()
    si = s_idx.pop()
    sj = s_idx.pop()
    ans += sj - si

if t_idx:
    print(-1)
    exit()

print(ans)




# ans = 0
# for i in range(n-1,0,-1):
#     if s[i] == 0 and t[i] == 1:
#         print(-1)
#         exit()
#     if s[i] == 1 and t[i] == 0:
#         ans += 1
#         s[i] = 0
#         s[i-1] = 1 - s[i-1]

# if s[0] == t[0]:
#     print(ans)
# else:
#     print(-1)