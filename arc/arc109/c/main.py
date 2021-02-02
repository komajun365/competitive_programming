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
s = input()
d = dict()
d['RR'] = 'R'
d['RS'] = 'R'
d['SR'] = 'R'
d['PP'] = 'P'
d['PR'] = 'P'
d['RP'] = 'P'
d['SS'] = 'S'
d['SP'] = 'S'
d['PS'] = 'S'

def calc(x):
    res = ''
    m = len(x)//2
    for i in range(m):
        res += d[ x[i*2:i*2+2] ]
    return res

x = s
for _ in range(k):
    if(len(x) % 2 == 1):
        x += x
    x = calc(x)

print(x[0])



