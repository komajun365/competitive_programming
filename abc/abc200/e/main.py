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

now = 0
for tot in range(n*3-2):
    if tot <= n-1 or tot >= (n-1)*2:
        t = min(tot, (n-1)*3 - tot)
        li,lc = 0, t+1
        ri,rc = t, 1
        new = (ri-li+1)*(lc+rc)//2
    else:
        li,lc = 0, n - abs((n-1)-tot)
        mi,mc = tot-(n-1), n
        ri,rc = n-1, n - abs((n-1)-(tot-(n-1)))
        new = (mi-li+1)*(lc+mc)//2 + (ri-mi+1)*(mc+rc)//2 - mc
    if now + new >= k:
        break
    now += new

for i in range(n):
    # print(i,now,tot)
    jk = tot - i
    if jk > (n-1)*2:
        continue
    new = n - abs(jk - (n-1))
    if now + new >= k:
        break
    now += new

for j in range(n):
    m = tot - i - j
    if m > n-1:
        continue
    now += 1
    if now == k:
        break
print(i+1,j+1,m+1)

