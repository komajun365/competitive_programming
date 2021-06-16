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

def get_point(l,r):
    # sqrt(2):1
    d = r-l
    res = l + round((r-l) / 2**0.5)
    return res

def solve():
    n = int(input())
    i = get_point(0,n+1)
    print('? {}'.format(i), flush=True)
    ai = int(input())
    idx = [0,i,n+1]
    num = [-1,ai,-1]
    while not (idx[2]-idx[1] == 1 and idx[1]-idx[0] == 1):
        if idx[2]-idx[1] > idx[1]-idx[0]:
            i = get_point(idx[0],idx[2])
            print('? {}'.format(i), flush=True)
            ai = int(input())
            if ai > num[1]:
                idx[0],idx[1] = idx[1],i
                num[0],num[1] = num[1],ai
            else:
                idx[2] = i
                num[2] = ai
        else:
            i = get_point(idx[0],idx[1])
            print('? {}'.format(i), flush=True)
            ai = int(input())
            if ai > num[1]:
                idx[1],idx[2] = i,idx[1]
                num[1],num[2] = ai,num[1]
            else:
                idx[0] = i
                num[0] = ai
    print('! {}'.format(num[1]), flush=True)

t = int(input())
for _ in range(t):
    solve()

