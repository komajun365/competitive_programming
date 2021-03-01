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

n = int(input())
a = list(map(int,input().split()))

single = set()
double = set()
for ai in a:
    if not ai in single:
        single.add(ai)
    else:
        if not ai in double:
            double.add(ai)

db = list(double)
db.sort()
if len(db) < 2:
    print(0)
else:
    if a.count(db[-1]) >= 4:
        print(db[-1]**2)
    else:
        print(db[-1] * db[-2])