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

n = int(readline())
ab = list(map(int,read().split()))

links = [[] for _ in range(n)]
it = iter(ab)
for a,b in zip(it,it):
    links[a].append(b)
    links[b].append(a)

root = 0
parent = [-2] * n
parent[root] = -1
ts = [root]
stack = [root]
while(stack):
    next = []
    while(stack):
        i = stack.pop()
        for j in links[i]:
            if(parent[j] != -2):
                continue
            ts.append(j)
            next.append(j)
            parent[j] = i
    stack = next[::]

root = ts[-1]
parent = [-2] * n
parent[root] = -1
ts = [root]
stack = [root]
while(stack):
    next = []
    while(stack):
        i = stack.pop()
        for j in links[i]:
            if(parent[j] != -2):
                continue
            ts.append(j)
            next.append(j)
            parent[j] = i
    stack = next[::]

ts = ts[::-1]
nums = [0] * n
for i in ts:
    cnt_0 = 0
    for j in links[i]:
        if(j == parent[i]):
            continue
        if(nums[j] == 0):
            cnt_0 += 1
        else:
            nums[i] += nums[j]
    nums[i] += max(0,cnt_0-1)

ans = nums[root]
if(len(links[root])==1):
    ans += 1

print(ans)



'''
なにこれ面白い！

頂点i,jにアンテナを置いたとき、
i-jのパス上にあるアンテナは確定できる。
それ以外は、iもしくはjに直線グラフが一本くっついているだけならそれは判定できる。
→　でもその場合、iにアンテナを置く意味はあまりない。

i,jにアンテナを置くとする。
i-jのパスは確定する。

そして、i-jのパス上の点には、すでにアンテナを置いたと考えても良い！
→　すべての端点を拾う、という上界が考えられる。
　　でもまだ減らせる。
　　直線パスは確定するので。

もしかして最大の次数で決まる？
→　だめでした。
　　でも、ほとんどイケてるので裏がありそう。


適当に値を決めて、
深いところからスタートする。
葉の値は0
親の数は、すべての子供の数字の合計＋(0の数-1)


なんか嘘解法っぽいぞ？？？
'''
