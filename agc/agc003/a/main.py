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
N = s.count('N')
W = s.count('W')
S = s.count('S')
E = s.count('E')
if (N*S == 0 and N+S > 0) or (W*E == 0 and W+E > 0):
    print('No')
else:
    print('Yes')