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
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m,*data = map(int,read().split())
a = [0] + data[:n]
b = [0] + data[n:n*2]
cd = data[2*n:]

links = [[] for _ in range(n+1)]
it = iter(cd)
for c,d in zip(it,it):
    links[c].append(d)
    links[d].append(c)

done = [0] * (n+1)
for i in range(1,n+1):
    if(done[i] == 1):
        continue

    tot_a = 0
    tot_b = 0
    done[i] = 1
    num_v = 1
    stack = [i]
    while(stack):
        k = stack.pop()
        tot_a += a[k]
        tot_b += b[k]
        for j in links[k]:
            if(done[j] == 1):
                continue
            done[j] = 1
            num_v += 1
            stack.append(j)
    
    # print(tot_a,tot_b)
    if(tot_a != tot_b):
        print('No')
        exit()

print('Yes')
