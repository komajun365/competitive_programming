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

a = input()
b = input()
c = input()
abc = [a,b,c]

base = ord('a')
abc2 = [[],[],[]]
for i in range(3):
    for si in abc[i]:
        if si =='?':
            abc2[i].append(-1)
        else:
            abc2[i].append( ord(si) - base)

match = []
for i in range(3):
    match.append([[] for _ in range(3)])
    for j in range(3):
        if i == j:
            continue
        li = len(abc2[i])
        lj = len(abc2[j])
        match[i][j] = [0] * (li+1)
        match[i][j][-1] = 1
        for i_idx in range(li):
            for j_idx in range(lj):
                if i_idx + j_idx == li:
                    match[i][j][i_idx] = 1
                    break
                if abc2[i][i_idx + j_idx] != abc2[j][j_idx] and \
                   abc2[i][i_idx + j_idx] != -1 and \
                   abc2[j][j_idx] != -1:
                    break               
            else:
                match[i][j][i_idx] = 1

ans = 6000
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        k = 3-i-j
        for i_idx in range(len(abc2[i]) + 1):
            for j_idx in range(max(len(abc2[j]) + 1, len(abc2[i])+1 - i_idx)):
                if match[i][j][min(i_idx, len(abc2[i]))] == 1 and \
                   match[i][k][min(i_idx+j_idx, len(abc2[i]))] == 1 and \
                   match[j][k][min(j_idx, len(abc2[j]))] == 1:
                    tmp = max(len(abc2[i]), i_idx + len(abc2[j]), i_idx+j_idx+len(abc2[k]))
                    ans = min(ans, tmp)

print(ans)

# for i in range(3):
#     for j in range(3):
#         print(match[i][j])



