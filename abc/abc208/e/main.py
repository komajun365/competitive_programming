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

n,k = map(int,input().split())
n = str(n)
l = len(n)
d1 = dict()
d2 = dict()
for i in range(1,int(n[0])):
    d2[i] = 1
d1[int(n[0])] = 1

for i in range(1,l):
    d11 = dict()
    d22 = dict()
    for key,val in d1.items():
        ni = n[i]
        for j in range(int(ni)):
            d22[key * j] = d22.get(key * j, 0) + val
        ni = int(ni)
        d11[key * ni] = d11.get(key * ni, 0) + val
    for key,val in d2.items():
        for j in range(10):
            d22[key * j] = d22.get(key * j, 0) + val
    for j in range(1,10):
        d22[j] = d22.get(j, 0) + 1
    
    d1,d11 = d11,d1
    d2,d22 = d22,d2
    # print(d1)
    # print(d2)

ans = 0
for key,val in d1.items():
    if key <= k:
        ans += val
for key,val in d2.items():
    if key <= k:
        ans += val
print(ans)




# print(54*36*18*18)
'''
2,3,5,7
54 * 36 * 18 * 18
少ない。

'''