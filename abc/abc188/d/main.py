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

n,C,*abc = map(int,read().split())

days = set()
days.add(0)
it = iter(abc)
for a,b,c in zip(it,it,it):
    days.add(a-1)
    days.add(b)

decode = list(days)
decode.sort()

encode = dict()
for i,di in enumerate(decode):
    encode[di] = i

imos = [0] * len(decode)
it = iter(abc)
for a,b,c in zip(it,it,it):
    a = encode[a-1]
    b = encode[b]
    imos[a] += c
    imos[b] -= c

for i in range(len(imos)-1):
    imos[i+1] += imos[i]

ans = 0
for i in range(len(imos)-1):
    wide = decode[i+1] - decode[i]
    ans += min(C,imos[i]) * wide

print(ans)



