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

n,d1,d2 = map(int,input().split())
n2 = n*2
v = n2**2

def calc(d,point):
    bad = []
    for i in range(n2):
        if i**2 > d:
            break
        for j in range(n2):
            d_ij = i**2 + j**2
            if d_ij > d:
                break
            elif d_ij == d:
                bad.append([i,j])
                break
    
    # print(bad)

    links = [[] for _ in range(v)]
    for i in range(n2):
        for j in range(n2):
            for x,y in bad:
                for mx,my in zip([1,1,-1,-1],[1,-1,1,-1]):
                    mx = mx*x + i
                    my = my*y + j
                    if 0 <= mx < n2 and 0 <= my < n2:
                        links[i*n2+j].append(mx*n2+my)

    # print(links)

    res = [-1] * v
    for i in range(v):
        if res[i] != -1:
            continue
        res[i] = 0
        stack = [i]
        while(stack):
            j = stack.pop()
            for k in links[j]:
                if res[k] != -1:
                    continue
                res[k] = (res[j] + point) % (point*2)
                stack.append(k)
    
    return res

g1 = calc(d1,1)
g2 = calc(d2,2)

g = [i+j for i,j in zip(g1,g2)]
for num in range(4):
    if g.count(num) >= n**2:
        break

ans = []
cnt = 0
for i in range(v):
    if g[i] == num:
        ans.append(str(i//n2) + ' ' + str(i%n2))
        cnt += 1
        if cnt == n**2:
            break

print('\n'.join(ans))

