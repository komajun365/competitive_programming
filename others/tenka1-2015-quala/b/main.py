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

n,*se = read().split()
n = int(n)

def decode(x):
    hh = int(x[:2])
    mm = int(x[3:5])
    ss = int(x[6:8])
    mmm = int(x[9:])
    # print(hh,mm,ss,mmm)
    hh -= 21
    res = ((hh*60 + mm)*60 + ss)*1000 + mmm

    return res

def encode(x):
    mmm = x % 1000
    x //= 1000
    ss = x % 60
    x //= 60
    mm = x % 60
    x //= 60
    hh = x+21
    hh = str(hh)
    mm = str(mm)
    ss = str(ss)
    mmm = str(mmm)
    mm = '0' * (2 - len(mm)) + mm
    ss = '0' * (2 - len(ss)) + ss
    mmm = '0' * (2 - len(mmm)) + mmm
    res = '{}:{}:{}.{}'.format(hh,mm,ss,mmm)
    return res

left = decode('20:00:00.000')
right = decode('23:00:00.000')

it = iter(se)
se2 = []
for s,e in zip(it,it):
    s = decode(s)
    e = decode(e)
    se2.append([s,e])
    if s >= e:
        left = max(left,s)
        right = min(right, e)

if left == decode('20:00:00.000') and right == decode('23:00:00.000'):
    for i in range(n):
        print(-1)
    exit()

left -= 1000
right += 1000
for s,e in se2:
    if s >= e:
        print(1000 + e - s)
    elif left < s < right or left < e < right:
        print(-1)
    elif s <= left and right <= e:
        print(e-s + 1000)
    else:
        print(e-s)



