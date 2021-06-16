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
read = sys.stdin.buffer.read

t,*abc = map(int,read().split())

def solve(a,b,c):
    if ((b | c) & ~a) > 0:
        return 'No'

    flag110 = (a & b & ~c) > 0
    flag111 = (a & b & c) > 0
    if flag110 and flag111:
        return 'No'
    
    return 'Yes'

ans = []
it = iter(abc)
for a,b,c in zip(it,it,it):
    ans.append(solve(a,b,c))

print('\n'.join(ans))

'''
a,b,c
000 -> ok
001 -> no
010 -> no
011 -> no
100 -> ok
101 -> ok
110 -> ok
111 -> ok

110と111両方はダメ



4,2,4
100
010
100

'''

