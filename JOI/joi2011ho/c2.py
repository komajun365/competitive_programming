# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討15分　実装15分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

def main():
    """ここに今までのコード"""
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    from heapq import heappop,heappush

    n,m,k = map(int,readline().split())
    data = list(map(int, read().split()))
    roads = data[:m*3]
    mall = data[m*3:]

    links = [[] for _ in range(n+1)]
    it = iter(roads)
    for a,b,c in zip(it,it,it):
        links[a].append((c,b))
        links[b].append((c,a))

    for a in mall:
        links[0].append((0,a))

    # dijkstra
    def dijkstra(links, start, n):
        inf = 10**7
        d = [inf] * (n)
        d[start] = 0
        hq = []
        used = set()
        used.add(start)
        for i in links[start]:
            heappush(hq, i)
        while(hq):
            cost,i = heappop(hq)
            if( i in used):
                continue
            d[i] = cost
            used.add(i)
            for tmp in links[i]:
                cost_next, j = tmp
                if(not j in used):
                    heappush(hq, (cost+cost_next, j))
        return d

    d = tuple(dijkstra(links, 0, n+1))

    ans = max(d)*2
    it = iter(roads)
    ans_d = [d[a]+d[b]+c for a,b,c in zip(it,it,it)]
    ans = max(ans, max(ans_d))

    print((ans+1)//2)

if __name__ == '__main__':
    main()


'''
実装
全ての街について最寄りのショッピングモールまでの距離dを求める。
その後、道路（町i,jを結ぶ、長さrdの道とする）ごとに
max(d[i],d[j],(d[i]+d[j]+rd)/2)を求めて最大値を得ればOK.

最寄りのショッピングモールまでの距離dについては、
全てのショッピングモールがある町からコスト0の道がはられた新しい町を一つ作ることで、
その新しい街を起点としたダイクストラ法によりo(M+NlogN)で求まる。

愚直に実装すると時間もメモリも厳しい。。。
'''
