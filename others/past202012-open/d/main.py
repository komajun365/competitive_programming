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

n,*data = read().split()
n = int(n)

s = []
for si in data:
    num_s = int(si)
    head = (len(si) - len(str(num_s))) * -1
    s.append([num_s, head, si])

s.sort()
print('\n'.join(map(lambda x:x[2], s)))

# print(s)