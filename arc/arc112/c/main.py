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

links = [[] for _ in range(n+1)]
for i,ai in enumerate(a,2):
    links[i].append(ai)
    links[ai].append(i)

root = 1
par = [-1] * (n+1)
par[root] = 0
stack = [root]
tp = []
while(stack):
    i = stack.pop()
    tp.append(i)
    for j in links[i]:
        if par[j] != -1:
            continue
        par[j] = i
        stack.append(j)

tp = tp[::-1]
children = [[] for _ in range(n+1)]

def calc(ch):
    res = [0,1]
    even_m = []
    odd = []
    for a,b in ch:
        if (a+b) % 2 == 0:
            if a > b:
                res[0] += a
                res[1] += b
            else:
                even_m.append([a,b])
        else:
            odd.append([a,b])
    odd.sort(key = lambda x: x[1]-x[0])
    l = len(odd)
    for i in range(l):
        a,b = odd[i]
        res[i%2] += a
        res[(i+1)%2] += b
    for a,b in even_m:
        res[l%2] += a
        res[(l+1)%2] += b
    return res

for i in tp:
    children[par[i]].append( calc(children[i]) )

ans = children[0][0][1]
print(ans)
# print(children)
    




