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

import heapq

n,k = map(int,input().split())
s = input()
if k < 2:
    print(s)
    exit()

idx = [[] for _ in range(26)]
for i,si in enumerate(s):
    idx[ord(si) - ord('a')].append(i)

pr = []
for i in idx:
    pr += i[::-1]

def make(x,y):
    use = set()
    for i in range(x):
        use.add(i)
    for i in range(y):
        use.add(pr[i])
    ch = []
    for i in use:
        ch.append(s[i])
    ch.sort(reverse=True)
    res = ''
    for i in range(n):
        if i in use:
            res += ch.pop()
        else:
            res += s[i]
    
    cnt = 0
    for i in range(n):
        if res[i] != s[i]:
            cnt += 1

    return cnt,res

ans = s[::]
for i in range(n):
    for j in range(n):
        cnt,res = make(i,j)
        if cnt <= k:
            ans = min(ans, res)

print(ans)





# for p in pr:
#     print(p, s[p])

# cnt = 0
# ans = list(s)
# done = 0




# def make(x):
#     cnt = 0
#     res = list(s)

#     use = set()
#     hq = []
#     change = []
#     pr_i = 0
#     for i in range(n):
#         if i in use:
#             continue
#         use.add(i)
#         heappush(hq, s[i])
#         cnt += 1
#         if cnt








ok = k
ng = n+1


'''


'''