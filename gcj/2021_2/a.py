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
# f = open('../../input.txt', 'r')
# sys.stdin = f

# tot = 0
# for i in range(1,101):
#     tot += 1/i
# print(tot)

t,n = map(int,input().split())

def solve():
    for i in range(1,n):
        print('M {} {}'.format(i,n), flush=True)
        res = int(input())
        if res != i:
            print('S {} {}'.format(i,res), flush=True)
            res = int(input())
    print('D', flush=True)
    res = int(input())
    return 0

for i in range(t):
    solve()
exit()

