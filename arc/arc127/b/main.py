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

def make3(x):
    res = ''
    for i in range(l):
        res += str(x%3)
        x //= 3
    res = res[::-1]
    return res

ans = []
for i in range(n):
    ans.append(make3(i + 3**(l-1)*2))

next_dic = {'0':'1', '1':'2', '2':'0'}
next_dic2 = {'0':'2', '1':'0', '2':'1'}

for i in range(n):
    x = ans[i]
    a1 = ''
    a2 = ''
    for j in range(l):
        a1 += next_dic[x[j]]
        a2 += next_dic2[x[j]]
    ans.append(a1)
    ans.append(a2)

print('\n'.join(ans))




