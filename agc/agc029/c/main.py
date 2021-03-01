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

def check(x):
    if x == 1:
        now = 0
        for ai in a:
            if now >= ai:
                return False
            now = ai
        return True

    use = [[0,0]]
    for ai in a:
        stack = [ai]
        while(stack):
            i = stack.pop()
            if i == 0:
                return False
            if use[-1][0] < i:
                use.append([i,1])
                break
            while use[-1][0] > i:
                use.pop()
            if use[-1][0] == i:
                if use[-1][1] < x:
                    use[-1][1] += 1
                else:
                    use.pop()
                    stack.append(i-1)
            else:
                use.append([i,2])
    return True

ok = n
ng = 0
while(ok-ng>1):
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)