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

b1 = [1,0]
b2 = [0,10]
b3 = [100,100]

xy = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            x = i*b1[0] + j * b2[0] + k* b3[0]
            y = i*b1[1] + j * b2[1] + k* b3[1]
            xy.append([x,y])

a = set()
b = set()
b_cnt = dict()
c = set()
d = set()
for x,y in xy:
    a.add(x)
    b.add(x-y)
    c.add(y)
    d.add(x+y)
    if x-y in b_cnt:
        b_cnt[x-y] += 1
    else:
        b_cnt[x-y] = 1

# print(len(a),len(b),len(c),len(d))
print(len(xy))
print('\n'.join(map(lambda x: ' '.join(map(str,x)),xy)))