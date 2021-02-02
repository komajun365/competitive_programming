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
p = list(map(int,input().split()))
links_in = [set() for _ in range(n)]
links_out = [set() for _ in range(n)]
out_deg = [0] * (n)

for i,pi in enumerate(p):
    pi -= 1
    links_in[i].add(pi)
    links_out[pi].add(i)
    out_deg[pi] += 1

neigh = [0] * n
grundy = [-1] * n
stack = []
for i in range(n):
    if(out_deg[i] == 0):
        stack.append(i)

while(stack):
    i = stack.pop()
    for j in range(50):
        if(neigh[i] >> j)&1:
            continue
        grundy[i] = j
        break
    for j in links_in[i]:
        neigh[j] |= (1 << grundy[i])
        links_out[j].remove(i)
        out_deg[j] -= 1
        if(out_deg[j] == 0):
            stack.append(j)
    
for i in range(n):
    if(grundy[i] == -1):
        x = i
        break

def test(x,cand):
    tp = [ list(links_out[x])[0] ]
    while( x != tp[-1]):
        tp.append( list(links_out[tp[-1]])[0] )
    neigh2 = neigh[::]
    grundy2 = grundy[::]
    tp_len = len(tp)

    for i in range(tp_len-1,-1,-1):
        v1 = tp[i]
        if(v1 == x):
            grundy2[v1] = cand
        else:
            for j in range(50):
                if(neigh2[v1] >> j)&1:
                    continue
                grundy2[v1] = j
                break
        v2 = tp[i-1]
        neigh2[v2] |= (1 << grundy2[v1])
        # print(v1,v2)

    # print(x,cand)
    # print(tp)
    # print(neigh2)
    # print(grundy2)

    for j in range(50):
        if(neigh2[x] >> j)&1:
            continue
        if(j == cand):
            print('POSSIBLE')
            exit()
        break

    return 0

cand = [-1,-1]
cnt = 0
for j in range(50):
    if(neigh[x] >> j)&1:
        continue
    test(x,j)
    cnt += 1
    if(cnt==2):
        break

print('IMPOSSIBLE')
    

    

        









