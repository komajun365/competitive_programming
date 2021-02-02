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

# n = int(input())
# c_aa = input()
# c_ab = input()
# c_ba = input()
# c_bb = input()

for i in range(16):
    cs = []
    for bi in range(4):
        if(i >> bi)&1:
            cs.append('B')
        else:
            cs.append('A')
    
    print(cs)

    s0 = set()
    s0.add('AB')
    for j in range(3,7):
        s1 = set()
        for si in s0:
            for k in range(len(si) -1):
                if(si[k] == 'A'):
                    if(si[k+1] == 'A'):
                        tmp = si[:k+1] + cs[0] + si[k+1:]
                    else:
                        tmp = si[:k+1] + cs[1] + si[k+1:]
                else:
                    if(si[k+1] == 'A'):
                        tmp = si[:k+1] + cs[2] + si[k+1:]
                    else:
                        tmp = si[:k+1] + cs[3] + si[k+1:]
                s1.add(tmp)
        s0,s1 = s1,s0
        print(j,len(s0))
    # print(len(s0))
    # print(s0)
                        