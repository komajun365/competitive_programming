# いわゆる全方位DP
# calc(a,calc(b,c)) == calc(calc(a,b),c) の時にうまくいくように作る。
# dpconのv4.pyとかを参考に。

# 前準備
import sys
input = sys.stdin.readline
from collections import deque

graph = [[] for _ in range()]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

ini = 'だいたい１で良いと思ってます'

# calcの定義 : 2辺を合わせる演算
def calc(a,b):
    return None

# dp1の更新
def calc1(c,p):
    #############
    # ここにいい感じに定義
    #############

    p_num = ini
    for i in graph[c]:
        if i == p:
            continue
        p_num = calc(p_num, dp1[i])
    dp1[c] = p_num % mod + 'なにか'

# dp2の更新　累積和チックにすることでうに対策。
def calc2(p):
    #############
    # ここにいい感じに定義
    #############
    arr = [dp1[c] if c != parent[p] else dp2[p] for c in graph[p]]

    left = [ini]
    for i in arr[:-1]:
        left.append( calc(left[-1], i ) )
    right = [ini]
    for i in arr[:0:-1]:
        right.append( calc(right[-1], i) )
    right = right[::-1]

    prod = []
    for a,b in zip(left,right):
        prod.append( calc(a,b) )

    for c,x in zip(graph[p], prod):
        if(c != parent[p]):
            dp2[c] = x + "なにか"



# 根から探索して親と探索順を記録
root = 1
order = []
parent = [0] * (n+1)
stack = deque()
stack.append(root)
while stack:
    x = stack.pop()
    order.append(x)
    for y in graph[x]:
        if y == parent[x]:
            continue
        stack.append(y)
        parent[y] = x

# 親→子の値を算出
dp1 = [0] * (n+1)
for i in order[::-1]:
    calc1(i, parent[i])

# 子→親の値を算出
dp2 = [0] * (n+1)
for i in order:
    calc2(i)

ans = 'ここに最終化の処理を書きましょう'
print(' '.join(map(str, ans)))
