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

s = input()
l = len(s)
left = 0
right = l
while left < l:
    if s[left] != 'a':
        break
    left += 1

while right > 0:
    if s[right-1] != 'a':
        break
    right -= 1

if right < left:
    print('Yes')
    exit()

if left > l-right:
    print('No')
    exit()

s2 = s[left:right]
s2_rev = s2[::-1]
if s2 == s2_rev:
    print('Yes')
else:
    print('No')
