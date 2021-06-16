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

'''
・n%4 == 1の時
最終形は
「a=0(mod 4)頂点の完全グラフ」＋「a=1(mod 4)頂点の完全グラフ」か、
「a=2(mod 4)頂点の完全グラフ」＋「a=3(mod 4)頂点の完全グラフ」で、
このとき辺の数は偶数。
Mが偶数なら後手の勝ち、
Mが奇数なら先手の勝ち。

・n%4 == 3の時
最終形は
「a=0(mod 4)頂点の完全グラフ」＋「a=3(mod 4)頂点の完全グラフ」か、
「a=2(mod 4)頂点の完全グラフ」＋「a=1(mod 4)頂点の完全グラフ」で、
このとき辺の数は奇数。
Mが偶数なら先手の勝ち、
Mが奇数なら後手の勝ち。

・n%4 == 0の時
最終形は
A：「a=0(mod 4)頂点の完全グラフ」＋「a=0(mod 4)頂点の完全グラフ」
B：「a=2(mod 4)頂点の完全グラフ」＋「a=2(mod 4)頂点の完全グラフ」
C：「a=1(mod 4)頂点の完全グラフ」＋「a=3(mod 4)頂点の完全グラフ」で、
A,Bは辺の数が偶数、Cは辺の数が奇数。

Mが偶数なら、A,Bに持ち込めば後手の勝ち
Mが奇数なら、A,Bに持ち込めば先手の勝ち





A,Bに持ち込む　＝　連結成分の頂点数を全部偶数にする、で達成可能
A,Bに持ち込みたい人は、頂点数奇数の連結成分をつなぐ、を基本的にはやり続ける。
Cに持ち込みたい人は、
「偶数、奇数、奇数」の状態にして、偶数と奇数を結ぶしかない。
これは、「奇数、奇数、奇数、奇数」の状態で相手に連結成分を潰してもらうしかない。
頂点数偶数と奇数をつなぐ、をやり続けて、偶数の数を減らすのがベストだが、
偶数の数が2個以上になるタイミングがあった瞬間に負け。


そうならないパターンを考えてみる。
・初期が奇数×10個、Mが奇数
先手はA,Bを目指す、後手はCを目指す
6手後に奇数×４になっている。
奇数×4の全辺の数は偶数なので、後手が連結成分をつぶすことになる。
→　後手の負け

・初期が奇数＊10個＋偶数1個、Mが偶数
先手はCを目指す、後手はA,Bを目指す
7手後に奇数×４になっている。
奇数×4の全辺の数は偶数なので、先手が連結成分をつぶすことになる。
→　先手の負け

いずれにせよ、連結成分が4以上なら
Mが偶数なら、後手の勝ち
Mが奇数なら、先手の勝ち

・n%4 == 2の時
最終形は
D：「a=1(mod 4)頂点の完全グラフ」＋「a=1(mod 4)頂点の完全グラフ」
E：「a=3(mod 4)頂点の完全グラフ」＋「a=3(mod 4)頂点の完全グラフ」
F：「a=0(mod 4)頂点の完全グラフ」＋「a=2(mod 4)頂点の完全グラフ」で、
A,Bは辺の数が偶数、Cは辺の数が奇数。

Mが偶数なら、Fに持ち込めば先手の勝ち
Mが奇数なら、Fに持ち込めば後手の勝ち

D,Eで勝ちたい人はやっぱり「奇数、奇数、奇数、奇数」に持ち込むしかない。

・初期が奇数×10個、Mが偶数
先手はFを目指す、後手はD,Eを目指す
6手後に奇数×4になっている
奇数×4の全辺の数は偶数なので、先手が連結成分をつぶすことになる。
→　先手の負け

・初期が奇数＊10個＋偶数1個、Mが奇数
先手はD,Eを目指す、後手はFを目指す
7手後に奇数×４になっている。
奇数×4の全辺の数は偶数なので、後手が連結成分をつぶすことになる。
→　後手の負け


ぐぐきき
ぐききぐ
ききぐぐ
きぐぐき

'''

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self,x):
        route = []
        while(x >= 0):
            route.append(x)
            x = self.parents[x]
        p = route.pop()
        for ri in route:
            self.parents[ri] = p
        return p

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
        if( self.parents[x_root] > self.parents[y_root] ):
            x_root,y_root = y_root,x_root
        self.parents[x_root] += self.parents[y_root]
        self.parents[y_root] = x_root

    def members(self,x):
        root = self.find(x)
        res = [ i for i in range(self.n) if self.find(i) == root ]
        return res

    def roots(self):
        res = [ i for i in range(self.n) if self.parents[i] < 0]
        return res

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        res = dict()
        for r in self.roots():
            res[r] = [r]
        for i in range(self.n):
            if not i in res:
                res[self.find(i)].append(i)
        return res
    
    def size_list(self):
        res = []
        for x in self.parents:
            if x < 0:
                res.append(x*-1)
        return res


import sys
read = sys.stdin.buffer.read

t,*data = map(int,read().split())

def solve(n,m,ab):
    if n%4 == 1:
        if m%2 == 0:
            return 'Second'
        else:
            return 'First'
    elif n%4 == 3:
        if m%2 == 0:
            return 'First'
        else:
            return 'Second'
    
    uf = UnionFind(n)
    it = iter(ab)
    for a,b in zip(it,it):
        a -= 1
        b -= 1
        uf.union(a,b)

    head = uf.size(0)
    tail = uf.size(n-1)

    if head % 2 == tail % 2 == 0:
        if n%4 == 0:
            if m%2 ==0:
                return 'Second'
            else:
                return 'First'
        else:
            if m%2 ==0:
                return 'First'
            else:
                return 'Second'
    elif head % 2 == tail % 2 == 1:
        if n%4 == 2:
            if m%2 ==0:
                return 'Second'
            else:
                return 'First'
        else:
            if m%2 ==0:
                return 'First'
            else:
                return 'Second'
    else:
        return 'First'

ans = []
idx = 0
for _ in range(t):
    n,m = data[idx:idx+2]
    ab = data[idx+2 : idx+2+2*m]
    idx += 2 + 2*m
    ans.append(solve(n,m,ab))

print('\n'.join(ans))