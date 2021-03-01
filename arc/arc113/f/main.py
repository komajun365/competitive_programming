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


def calc(left, mid ,right):
    l = left + mid + right
    l2 = l/2
    res = 0
    if left > l2:
        res = right + mid/2
    elif right > l2:
        res = left + mid/2
    else:
        ml = l2-left
        mr = l2-right
        res = (left + ml/2) * ml/mid + (right + mr/2) * mr/mid
    return res

