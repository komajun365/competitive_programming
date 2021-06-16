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

n = 7
done = set()
base = tuple(range(1,n+1))
done.add(base)
stack = [base]

while stack:
    i = stack.pop()
    for j in range(n-2):
        new = list(i[::])
        new[j] = -1 * i[j+2]
        new[j+1] = -1 * i[j+1]
        new[j+2] = -1 * i[j]
        new = tuple(new)
        if new in done:
            continue
        done.add(new)
        stack.append(new)

done = list(done)
done.sort()

print(len(done))
for i in done:
    if sum(i) == 28:
        print(i)

