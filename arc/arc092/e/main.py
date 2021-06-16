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

if max(a) < 0:
    max_num = max(a)
    for i in range(n):
        if a[i] == max_num:
            break
    ans = []
    for j in range(n,i+1,-1):
        ans.append(j)
    for j in range(i):
        ans.append(1)
    print(max_num)
    print(len(ans))
    print('\n'.join(map(str,ans)))
    exit()

use = [0] * n
tot = [0,0]
for i in range(n):
    if a[i] >= 0:
        use[i] = 1
        tot[i%2] += a[i]

if tot[0] > tot[1]:
    for i in range(n):
        if i % 2 == 1:
            use[i] = 0
else:
    for i in range(n):
        if i % 2 == 0:
            use[i] = 0

ans = []
idx = 0
while idx < n:
    if use[idx] == 0:
        ans.append(1)
        idx += 1
    else:
        r = idx+1
        while r < n:
            if use[r] == 1:
                break
            r += 1
        
        if r == n:
            for i in range(r-idx,1,-1):
                ans.append(i)
        else:
            between = r-idx - 1
            for i in range(between//2):
                ans.append(3)
            ans.append(2)
        idx = r
    # print('idx',idx)

print(max(tot))
print(len(ans))
print('\n'.join(map(str,ans)))




# cs = [0] * (n+2)
# for i in range(n):
#     cs[i] = cs[i-2] + a[i]

# inf = 10 ** 15
# max_num = inf * -1
# mins = [inf,inf]
# mins_idx = [-1,-1]
# lr = [-1,-1]
# for i in range(n):



# odd = a[1::2]
# even = a[::2]

# cs_odd = [0] * (len(odd)+1)
# cs_even = [0] * (len(even)+1)
# for i in range(len(odd)):
#     cs_odd[i] = cs_odd[i-1] + odd[i]
# for i in range(len(even)):
#     cs_even[i] = cs_even[i-1] + even[i]

# print(cs_odd)
# print(cs_even)