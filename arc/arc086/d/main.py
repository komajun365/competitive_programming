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

abs_max = [0,-1]

for i,ai in enumerate(a):
    if abs(ai) >= abs_max[0]:
        abs_max = [abs(ai), i]

ans = []
for i in range(n):
    if i != abs_max[1]:
        ans.append('{} {}'.format(abs_max[1]+1, i+1))

if a[abs_max[1]] >= 0:
    for i in range(n-1):
        ans.append('{} {}'.format(i+1,i+2))
else:
    for i in range(n-1,0,-1):
        ans.append('{} {}'.format(i+1,i))

print(len(ans))
print('\n'.join(ans))

