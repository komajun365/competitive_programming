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
s = list(map(int,input().split()))
s.sort(reverse=True)

now = [s[0]]
s[0] = -1
for i in range(n):
    max_num = 2**i
    idx = 0
    under = []
    for j,sj in enumerate(s):
        if(sj == -1):
            continue
        if(now[idx] > sj):
            under.append(sj)
            idx += 1
            s[j] = -1
        if(idx >= max_num):
            break
    else:
        print('No')
        exit()
    
    next = []
    now.append(-1)
    under.append(-1)
    ni = 0
    ui = 0
    while(ni < max_num) or (ui < max_num):
        if(now[ni] > under[ui]):
            next.append(now[ni])
            ni += 1
        else:
            next.append(under[ui])
            ui += 1
    now,next = next,now

print('Yes')






# tree = [0] * 2**(n+1)
# tree[0] = 10**10
# rem = [[] for _ in range(n+1)]
# rem[0] = [1]
# for i in range(1,n+1):
#     tmp = list(range(2**i + 1, 2**(i+1),2))
#     rem[i] = tmp[::-1]

# for si in s:
#     for h in range(n+1):
#         if(len(rem[h]) == 0):
#             continue
#         i = rem[h][-1]
#         p = i//2
#         if(tree[p] == si):
#             continue
#         rem[h].pop()
#         while(i < 2**(n+1)):
#             tree[i] = si
#             i *= 2
#         break
#     else:
#         print('No')
#         # print(si)
#         # print(rem)
#         # print(tree)
#         exit()

# print('Yes')

# idx = 0
# for bi in range(n,-1,-1):
#     for i in range(0,2**n,2**bi):
#         if(leaf[i] == 0):
#             leaf[i] = s[idx]
#             idx += 1

# print(leaf)

# def check(x):
#     it = iter(x)
#     res = []
#     for a,b in zip(it,it):
#         if(a <= b):
#             print('No')
#             exit()
#         res.append(a)
#     return res

# while(len(leaf) >= 2):
#     leaf = check(leaf)

# print('Yes')
