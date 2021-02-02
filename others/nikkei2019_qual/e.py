# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**9)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self,x):
        if(self.parents[x] < 0):
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def size(self, x):
        return self.parents[ self.find(x) ] * -1

    def same(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        return (x_root == y_root)

    def union(self,x,y):
        x_root = self.find(x)
        y_root = self.find(y)
        if(x_root == y_root):
            return

        #　番号が大きい方を新しい根にする
        if( x_root > y_root ):
            self.parents[x_root] += self.parents[y_root]
            self.parents[y_root] = x_root
        else:
            self.parents[y_root] += self.parents[x_root]
            self.parents[x_root] = y_root

    def members(self,x):
        root = self.find(x)
        ret = [ i for i in range(self.n) if self.find(i) == root ]
        return ret

    def roots(self):
        ret = [ i for i in range(self.n) if self.parents[i] < 0]
        return ret

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

n,m = map(int,readline().split())
x = list(map(int,readline().split()))
aby = list(map(int,read().split()))

edges = []
it = iter(aby)
for a,b,y in zip(it,it,it):
    edges.append((y,a,b))
edges.sort()

n_bi = n*2
bitree = [[0,-1,-1,-1,0] for _ in range(n_bi)]
for i,xi in enumerate(x,1):
    bitree[i][0] = xi

uf = UnionFind(n_bi)

e_ind = 0
for i in range(n+1,n_bi):
    while(True):
        e1 = edges[e_ind][1]
        e2 = edges[e_ind][2]
        if(uf.same(e1,e2)):
            e_ind += 1
            continue
        break

    left = uf.find(e1)
    right = uf.find(e2)
    edge_cost = edges[e_ind][0]

    bitree[i] = [bitree[left][0] + bitree[right][0],
                 -1,
                 left,
                 right,
                 edge_cost]
    bitree[left][1] = i
    bitree[right][1] = i

    uf.union(left,i)
    uf.union(right,i)

tree_group = [-1] * (n+1)
tree_group_cost = []
tree_group_ind = -1
stack = [n_bi-1]
while(stack):
    i = stack.pop()
    if(bitree[i][0] >= bitree[i][4]):
        #連結
        tree_group_ind += 1
        tree_group_cost.append(bitree[i][0])
        stack2 = [i]
        while(stack2):
            j = stack2.pop()
            if(j > n):
                stack2.append(bitree[j][2])
                stack2.append(bitree[j][3])
            else:
                tree_group[j] = tree_group_ind
    else:
        #非連結
        stack.append(bitree[i][2])
        stack.append(bitree[i][3])

ans = 0
for y,a,b in edges:
    if(tree_group[a]==tree_group[b]):
        tg = tree_group[a]
        if(tree_group_cost[tg] >= y):
            ans += 1

ans = m - ans
print(ans)


'''
逆かな？
いや、だめか。

連結成分を見つける
頂点の合計より大きい辺があれば削除する

を繰り返せばそのうち達成されるけど。。。
O(NM)になってしまいそう。

頂点と辺を逆転できないか？
→　無理め


二分探索できる？
→　できない。単調でない。

最初連結されているのは重要？

とりあえず最小全域木を作ってみる。
これのどこかの辺を削除したときに、それぞれの連結成分の頂点の合計値をO(1)で管理したい。

オイラーツアーかしら。



これでコストが問題なければOK。
あとは、追加できる辺を全部突っ込む。

コストオーバーの辺があった時、
問題のある辺

=======================

頂点数2n-1の二部木をボトムアップに作っていきます。
全ての葉は元のグラフの頂点を表します。
情報として、下記を持たせましょう。
(cost, parent, left,right, edge_cost)
葉の場合はleft,right=-1、lr_edge_cost=0　とします。

二部木の作り方はこうです。基本的には最小全域木の作り方＋αです。
要素数2n（0を使わないので実質2n-1）のUFを用意します。
元のグラフのM辺から最もコストの安い辺を持ってきます。
この辺をつなぐことで、連結成分が減るのであれば採用です。
つなぐedgeをe1,e2としましょう。
そこまでに構成した二部木の中で、
e1から辿った最も上部の頂点がleft
e2から辿った最も上部の頂点がrightです。
二部木の上の新しい頂点xを持ってきます。
今までのどの頂点よりも大きい点をpointerで管理すればよいでしょう。
・二部木の更新
bitree[x] = [bitree[left][0] + bitree[right][0],
             -1,
             left,
             right,
             (辺のコスト)]
bitree[left][1] = x
bitree[right][1] = x

・UFの更新
union(left,x)
union(right,x)
※UFの処理をいじって、親の値がグループ内での最大値になるようにしておく。
　上記のleft,right取得用。

・二部木ができたら
根から見ていきます。
costとedge_costを見比べて、
・cost >= edge_cost
この部分木は連結成分として成立します！

・cost < edge_cost
この部分木は連結成分として使えません。
子供たちについて、同じ処理をしてあげましょう。

→→すると、最終的なグラフの連結成分を知ることができます。

・最後に
連結成分ごとに、採用できる辺の数をカウントします。
最後にこれをmから引けば答えです。

長すぎ。

'''
