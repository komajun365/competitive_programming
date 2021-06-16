# lowlink
# 橋、関節点、二重辺連結成分分解など

def lowlink(links):
    n = len(links)
    order = [-1] * n
    low = [n] * n
    parent = [-1] * n
    child = [[] for _ in range(n)]
    roots = set()
    x = 0
    for root in range(n):
        if order[root] != -1:
            continue
        roots.add(root)
        stack = [root]
        parent[root] = -2
        while stack:
            i = stack.pop()
            if i >= 0:
                if order[i] != -1:
                    continue
                order[i] = x
                low[i] = x
                x += 1
                if i != root:
                    child[parent[i]].append(i)
                stack.append(~i)
                check_p = 0
                for j in links[i]:
                    if j == parent[i] and check_p == 0:
                        check_p += 1
                        continue
                    elif order[j] != -1:
                        low[i] = min(low[i], order[j])
                    else:
                        parent[j] = i
                        stack.append(j)
            else:
                i = ~i
                if i == root:
                    continue
                p = parent[i]
                low[p] = min(low[p], low[i])
    
    return order,low,roots,child

def get_articulation(links):
    n = len(links)
    order,low,roots,child = lowlink(links)
    articulation = [0] * n
    for i in range(n):
        if i in roots:
            if len(child[i]) >= 2:
                articulation[i] = 1
            continue
        for j in child[i]:
            if order[i] <= low[j]:
                articulation[i] = 1
                break
    
    return articulation

def get_bridge(links):
    n = len(links)
    order,low,roots,child = lowlink(links)
    bridge = []
    for root in roots:
        stack = [root]
        while stack:
            i = stack.pop()
            for j in child[i]:
                if order[i] < low[j]:
                    bridge.append([i,j])
                stack.append(j)
    
    return bridge

def two_edge_connected_componets(links):
    n = len(links)
    order,low,roots,child = lowlink(links)
    
    components = [-1] * n
    new_edges = []
    x = 0
    for root in roots:
        components[root] = x
        stack = [root]
        while stack:
            i = stack.pop()
            for j in child[i]:
                if order[i] < low[j]:
                    x += 1
                    components[j] = x
                    new_edges.append([components[i],x])
                else:
                    components[j] = components[i]
                stack.append(j)        
        x += 1
    
    return components,new_edges