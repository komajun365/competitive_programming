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

n,l = map(int,input().split())
a = [0] + list(map(int,input().split())) + [l+1]
b = [0] + list(map(int,input().split())) + [l+1]

s = []
g = []
for i in range(n+1):
    s.append(a[i+1]-a[i]-1)
    g.append(b[i+1]-b[i]-1)

ind = [0]
i = 0
for j in range(n+1):
    tmp = 0
    while(i < n+1):
        if(tmp < g[j]):
            tmp += s[i]
            i += 1
        else:
            break
    if(tmp != g[j]):
        print(-1)
        exit()
    ind.append(i)

ans = 0
for i in range(n+1):
    if(g[i] == 0):
        continue
    l = ind[i]
    while(s[l]==0):
        l += 1
    r = ind[i+1]-1
    ans += max(0, i-l)
    ans += max(0, r-i)
print(ans)
# print(ind)
# print(s)
# print(g)
# 
# ans = 0
# j = 0
# for i in range(n):
#     j = max(j, i+1)
#     if(s[i] > g[i]):
#         if(g[i] == 0):
#             s[i+1] += s[i]
#             s[i] = 0
#             ans += 1
#             continue
#         else:
#             print(-1)
#             exit()
#     elif(s[i] == g[i]):
#         continue
#     while(j < n+1):
#         if(s[i] < g[i]):
#             s[i] += s[j]
#             s[j] = 0
#             j += 1
#         else:
#             break
#     ans += j-1-i
#     if(s[i] > g[i]):
#         print(-1)
#         exit()

# if(s[-1] == g[-1]):
#     print(ans)
# else:
#     print(-1)
    



