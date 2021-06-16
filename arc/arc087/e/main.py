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

import sys
read = sys.stdin.read

n,l,*s = read().split()
n = int(n)
l = int(l)

s.append('')
s.sort()
s.append('')
dup = []
for i in range(n+1):
    l1 = len(s[i])
    l2 = len(s[i+1])
    j = 0
    for j in range(min(l1,l2)):
        if s[i][j] != s[i+1][j]:
            break
    dup.append(j)
dup[0] = -1
dup[-1] = -1

xor = 0
for i in range(1,n+1):
    l1 = len(s[i])
    for d in range(dup[i-1]+1, l1):
        if s[i][d] == '1':
            height = l - d
            cnt = 0
            while height > 0:
                if height & 1:
                    break
                height //= 2
                cnt += 1
            xor ^= 1 << cnt
    for d in range(dup[i]+1, l1):
        if s[i][d] == '0':
            height = l - d
            cnt = 0
            while height > 0:
                if height & 1:
                    break
                height //= 2
                cnt += 1
            xor ^= 1 << cnt

if xor == 0:
    print('Bob')
else:
    print('Alice')


# if (cnt[1]+cnt[3]) % 2 == 1:
#     print('Alice')
# elif cnt[1] % 2 == 1 and cnt[3] % 2 == 1:
#     print('Alice')
# else:
#     if (cnt[0] + cnt[2]) % 2 == 1:
#         print('Alice')
#     else:
#         print('Bob')



# print(s)
# print(dup)
# print(cnt)

