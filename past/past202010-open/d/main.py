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
s = input() + '#'

ans = []
tmp = 0
for si in s:
    if(si == '#'):
        ans.append(tmp)
        tmp = 0
    else:
        tmp += 1
x = ans[0]
y = ans[-1]
max_num = max(ans)
if(x+y < max_num):
    x = max_num-y
print('{} {}'.format(x,y))
# print(ans)