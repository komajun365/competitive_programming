# import
# import numpy as np
# from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
# from scipy.sparse import csr_matrix

# version的に使えないかも・・・


# # dijkstra
# import heapq
# def dijkstra(links, start, n):
#     inf = 10**10
#     d = [inf] * (n)
#     d[start] = 0
#     hq = []
#     for i in links[start]:
#         heapq.heappush(hq, i)
#     while(hq):
#         cost,i = heapq.heappop(hq)
#         if( d[i] != inf):
#             continue
#         d[i] = cost
#         for tmp in links[i]:
#             cost_next, j = tmp
#             if(d[j] == inf):
#                 heapq.heappush(hq, (cost+cost_next, j))
#     return d

# dijkstra
import heapq
def dijkstra(links, start, n):
    inf = 10**10
    d = [inf] * (n)
    d[start] = 0
    hq = []
    for cost,i in links[start]:
        heapq.heappush(hq, cost*inf + i)
    while(hq):
        num = heapq.heappop(hq)
        cost = num//inf
        i = num%inf
        if( d[i] != inf):
            continue
        d[i] = cost
        for tmp in links[i]:
            cost_next, j = tmp
            if(d[j] == inf):
                heapq.heappush(hq, inf*(cost+cost_next)+j )
    return d

# bellman_ford
# 負の経路がある場合は、(-1,-1)を返却する
# start→endに無関係な閉路に反応してしまう可能性あり。abc137のe問題例3がわかりやすい。
def bellman_ford(links, start, end, n):
    inf = 10**10
    d = [inf] * (n+1)
    d[start] = 0
    parent = [-1] * (n+1)

    for _ in range(n):
        update = False
        for i in range(1,n+1):
            for j in links[i]:
                cost,neigh = j
                if(d[neigh] > d[i] + cost):
                    d[neigh] = d[i] + cost
                    parent[neigh] = i
                    update = True

        if(not update):
            # 経路の算出
            route = [end]
            now = end
            while(now != start):
                now = parent[now]
                route.append(now)

            return d,route[::-1]

    # 負の閉路がある場合（n-1回の更新で終わらない場合）
    return -1,-1

# m行の入力から1~nまでのedgeのコスト情報付きlinksを作る
# directed:無向グラフならFalse、有向グラフならTrue
def make_links_cost(n,m, directed=False):
    links = [[] for _ in range(n+1)]
    if(directed):
        for _ in range(m):
            a,b,c = map(int, input().split())
            links[a].append((c,b))
    else:
        for _ in range(m):
            a,b,c = map(int, input().split())
            links[a].append((c,b))
            links[b].append((c,a))

    return links


# ワーシャルフロイド
def warshall_floyd(d,n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

# m行の入力から距離を値に持つ隣接行列を作成 0-indexed
# directed:無向グラフならFalse、有向グラフならTrue
def make_d_matrix(n,m,directed=False):
    inf = 10**13
    d = [[inf] * n for _ in range(n)]
    if(directed):
        for _ in range(m):
            a,b,c = map(int, input().split())
            d[a-1][b-1] = c
    else:
        for _ in range(m):
            a,b,c = map(int, input().split())
            d[a-1][b-1] = c
            d[b-1][a-1] = c




######################################################
# scipy 使う場合

# dijkstra
