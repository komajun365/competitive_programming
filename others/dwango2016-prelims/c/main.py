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
# dijkstra
import heapq
def dijkstra(links, start, n):
    inf = 1<<30
    d = [inf] * (n)
    d[start] = 0
    hq = []
    for x in links[start]:
        cost,i = divmod(x,base)
        heapq.heappush(hq, cost*base + i)
    while(hq):
        num = heapq.heappop(hq)
        cost,i = divmod(num,base)
        if( d[i] != inf):
            continue
        d[i] = cost
        for tmp in links[i]:
            cost_next, j = divmod(tmp, base)
            if(d[j] == inf):
                heapq.heappush(hq, base*(cost+cost_next)+j )
    return d

n,m,src,dst,*data = map(int,read().split())

L = 0
lines = [] # from,to,cost1,end,cost2
idx = 0
for _ in range(m):
    l = data[idx]
    idx += 1
    s = data[idx:idx+l]
    idx += l
    w = data[idx:idx+l-1]
    idx += l-1

    end = s[0]
    c_end = 0
    for i in range(l-1):
        a,b = s[i:i+2]
        c = w[i]
        c_end += c
        lines.append([b,a,c,end,c_end])
    end = s[-1]
    c_end = 0
    for i in range(l-2,-1,-1):
        a,b = s[i:i+2]
        c = w[i]
        c_end += c
        lines.append([a,b,c,end,c_end])

# print(lines)

base = 1<<20
inf = 1<<30

n2 = n*2 + len(lines)
links = [[] for _ in range(n2)]
for i in range(len(lines)):
    fr,to,c1,end,c2 = lines[i]
    links[fr].append((c1 << 20) + to)
    links[fr].append((c2 << 20) + 2*n + i)
    links[2*n + i].append(end + n)
    links[fr+n].append((c1 << 20) + to + n)

d_src = dijkstra(links, src, n2)
d_dst = dijkstra(links, dst+n, n2)

# print(d_src)
# print(d_dst)

cost_line = []
for i in range(len(lines)):
    fr,to,c1,end,c2 = lines[i]
    cost = d_src[i+2*n] + d_dst[end+n]
    cost_line.append( (cost << 20) + i)
cost_line.sort()

near_v = [i % (1 << 20) for i in cost_line]
near_cost = [i >> 20 for i in cost_line]

ng = 0
ok = len(lines)
mid = len(lines)+10
links2 = [[] for _ in range(n)]
while ok - ng > 1:
    mid2 = (ok+ng)//2
    if mid > mid2:
        links2 = [[] for _ in range(n)]
        mid,mid2 = mid2,0
    else:
        mid,mid2 = mid2,mid
    for i in range(mid2,mid):
        v = near_v[i]
        fr,to,c1,end,c2 = lines[v]
        links2[fr].append(to)
    
    flag = False
    done = [0] * n
    done[src] = 1
    stack = [src]
    while len(stack) > 0 and flag == False:
        i = stack.pop()
        for j in links2[i]:
            if done[j] == 1:
                continue
            if j == dst:
                flag = True
                break
            done[j] = 1
            stack.append(j)
    
    if flag:
        ok = mid
    else:
        ng = mid

print(near_cost[ok-1])

# print(near_cost)
# print(near_v)
# print(ok)
# print(lines)

# links = [[] for _ in range(n)]

# lines = dict()
# ends = set()

# base = 1<<20
# inf = 1<<30

# idx = 0
# for _ in range(m):
#     l = data[idx]
#     idx += 1
#     s = data[idx:idx+l]
#     idx += l
#     w = data[idx:idx+l-1]
#     idx += l-1

#     for i in range(l-1):
#         a,b = s[i:i+2]
#         links[a].append((w[i] << 20) + b)
#         links[b].append((w[i] << 20) + a)
#         links_end[a].append((w[i] << 20) + b)
#         links_end[b].append((w[i] << 20) + a)
    
#     if s[0] in lines:
#         lines[s[0]].append(s[::-1])
#     else:
#         lines[s[0]] = [s[::-1]]
#         ends.add(s[0])
#     if s[-1] in lines:
#         lines[s[-1]].append(s[::])
#     else:
#         lines[s[-1]] = [s[::]]
#         ends.add(s[-1])

#     cost = 0
#     end = s[0] + n
#     for i in range(l-1):
#         j = s[i+1]
#         cost += w[i]
#         links_end[j].append((cost << 20) + end)
#     cost = 0
#     end = s[-1] + n
#     for i in range(l-2,-1,-1):
#         j = s[i]
#         cost += w[i]
#         links_end[j].append((cost << 20) + end)

# d_src = dijkstra(links_end, src, n*2)
# d_dst = dijkstra(links, dst, n)

# # print(d_src)
# # print(d_dst)

# near_end = []
# for i in ends:
#     cost = d_src[i+n] + d_dst[i]
#     near_end.append((cost<<20) + i)

# near_end.sort()
# end_num = len(near_end)
# near_v = [i % (1 << 20) for i in near_end]
# near_cost = [i >> 20 for i in near_end]

# ng = 0
# ok = end_num
# mid = end_num
# links2 = [[] for _ in range(n)]
# while ok - ng > 1:
#     mid2 = (ok+ng)//2
#     if mid > mid2:
#         links2 = [[] for _ in range(n)]
#         mid = mid2
#         for i in range(mid):
#             for line in lines[near_v[i]]:
#                 l = len(line)
#                 for j in range(l-1):
#                     a,b = line[j:j+2]
#                     links2[a].append(b)
#     else:
#         for i in range(mid,mid2):
#             for line in lines[near_v[i]]:
#                 l = len(line)
#                 for j in range(l-1):
#                     a,b = line[j:j+2]
#                     links2[a].append(b)
#         mid = mid2
    
#     flag = False
#     done = [0] * n
#     done[src] = 1
#     stack = [src]
#     while len(stack) > 0 and flag == False:
#         i = stack.pop()
#         for j in links2[i]:
#             if done[j] == 1:
#                 continue
#             if j == dst:
#                 flag = True
#                 break
#             done[j] = 1
#             stack.append(j)
    
#     if flag:
#         ok = mid
#     else:
#         ng = mid

# print(near_cost[ok-1])
# print(near_cost)
# print(near_v)
# print(ok)
# print(lines)






    