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

# import random
# n = random.randint(2,10)
# p = [random.randint(1,n) for _ in range(n)]
# for i in range(n):
#     if(p[i] == i+1):
#         p[i] = (p[i] -1)%10 + 1
# n = 10
# p =  [2, 1, 1, 7, 8, 9, 6, 10, 2, 6]

# print(n,p)

n = int(input())
p = list(map(int,input().split()))

out = [0] * n
links_in = [set() for _ in range(n)]
links_out = [set() for _ in range(n)]
for i,pi in enumerate(p):
    pi -= 1
    links_in[i].add(pi)
    links_out[pi].add(i)
    out[pi] += 1

stack = []
for i,oi in enumerate(out):
    if(oi==0):
        stack.append(i)
neigh = [0] * n
g_num = [-1] * n

while(stack):
    i = stack.pop()
    for j in range(50):
        if(neigh[i] >>j)&1:
            continue
        g_num[i] = j
        break
    # print(i,g_num)
    # print(neigh)
    for j in links_in[i]:
        neigh[j] |= 1<<g_num[i]
        links_out[j].remove(i)
        out[j] -= 1
        if(out[j] == 0):
            stack.append(j)

x = -1
for i in range(n):
    if(g_num[i] == -1):
        x = i
        break

def check(x,num,num2):
    y = list(links_out[x])[0]
    i = list(links_in[x])[0]
    bef = x
    g_num2 = g_num[::]
    g_num2[x] = num
    flag = 1
    while(flag):
        if(i==x):
            flag -= 1

        ni = neigh[i]
        ni |= (1 << g_num2[bef])
        # print(i,ni)
        for j in range(50):
            if(ni >>j)&1:
                continue
            g_num2[i] = j
            break

        i,bef = list(links_in[i])[0],i
        
        # print(bef,i,g_num2)
    
    if(num == g_num2[x]):
        print('POSSIBLE')
        exit()
    
    # if(num < num2):
    #     if(g_num2[x] != g_num2[y]):
    #         print('POSSIBLE')
    #         exit()
    # else:
    #     if(g_num2[y] == num2):
    #         print('POSSIBLE')
    #         exit()

    return 0

cnt = 0
cand = [0,0]
for j in range(50):
        if(neigh[x] >j)&1:
            continue
        cand[cnt] = j
        cnt += 1
        if(cnt==2):
            break

check(x,cand[0],cand[1])
check(x,cand[1],cand[0])
print('IMPOSSIBLE')







