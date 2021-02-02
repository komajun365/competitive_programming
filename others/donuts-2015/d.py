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
from heapq import heappop,heappush

n,k = map(int,readline().split())
c = [0] + list(map(int,readline().split())) + []
q = int(readline())
d = []
if(q>0):
    d = list(map(int,read().split()))

left = [0] * (n+2)
right = [0] * (n+2)

c2 = [ (ci,i) for i,ci in enumerate(c)]
c2.sort()

dif = []
for i in range(1,n):
    ci,i_ind = c2[i]
    cj,j_ind = c2[i+1]
    dif.append(cj-ci)
    right[i_ind] = j_ind
    left[j_ind] = i_ind

ci,i_ind = c2[1]
left[i_ind] = 0
right[0] = i_ind

ci,i_ind = c2[n]
left[n+1] = i_ind
right[i_ind] = n+1

dif.sort()
mins = [0]
rem = []
for i in range(n-k):
    heappush(mins, -1 * dif[i])
for i in range(n-k,len(dif)):
    heappush(rem, dif[i])
tot = -1 * sum(mins)

mins_out = []
rem_out = []
ans = [tot]

def min_pop():
    while(mins_out):
        if(mins_out[0] == mins[0]):
            heappop(mins_out)
            heappop(mins)
        else:
            break
    return heappop(mins)

def rem_pop():
    while(rem_out):
        if(rem_out[0] == rem[0]):
            heappop(rem_out)
            heappop(rem)
        else:
            break
    return heappop(rem)

for di in d:
    l_ind = left[di]
    r_ind = right[di]
    if(l_ind==0)|(r_ind==n+1):
        if(l_ind==0):
            a = c[r_ind] - c[di]
            left[r_ind] = 0
        else:
            a = c[di] - c[l_ind]
            right[l_ind] = n+1

        min_max = min_pop() * -1
        if( a <= min_max ):
            #緩衝材グループ
            heappush(mins,min_max*-1)
            heappush(mins_out, a*-1)
            tot -= a
        else:
            heappush(rem,min_max)
            heappush(rem_out,a)
            tot -= min_max
    else:
        a = c[di] - c[l_ind]
        b = c[r_ind] - c[di]
        left[r_ind] = l_ind
        right[l_ind] = r_ind

        a,b = min(a,b),max(a,b)
        heappush(rem,a+b)
        min_max = min_pop() * -1
        min_max2 = min_pop() * -1
        if(a <= min_max2)&(b <= min_max):
            #二つとも緩衝材
            heappush(mins_out,a * -1)
            heappush(mins_out,b * -1)
            heappush(mins,min_max * -1)
            heappush(mins,min_max2 * -1)
            add = rem_pop()
            heappush(mins,-1 * add)
            tot -= a+b
            tot += add
        elif(a <= min_max):
            #一つだけ緩衝材
            heappush(mins_out,a * -1)
            heappush(rem_out,b)
            heappush(mins,min_max * -1)
            heappush(mins,min_max2 * -1)
            tot -= a
        else:
            #二つともあまり
            heappush(rem_out,a)
            heappush(rem_out,b)
            heappush(rem,min_max)
            heappush(mins,min_max2 * -1)
            tot -= min_max
    ans.append(tot)

print('\n'.join(map(str,ans)))







'''
箱がN個、ドーナツがK個
緩衝材を入れるのはn-k個

小さい順に並べて、
体積差が小さい奴からとっていけばよい

・箱をつぶす
体積差が統合されて新しい奴ができる。

箱がつぶれ、
a,bが消え、a+bができたとする。
この時、緩衝材グループの数がx個だったとしよう。

・a,bともに緩衝材だった
a+bを余りグループに追加。
ansからa+bを引く。
その後、余りグループから一つ緩衝材グループに1個追加する。
緩衝材グループのサイズはx+1になる。
以後、緩衝材グループからa,bが出てきた場合は一個スキップする。

・aだけが緩衝材だった
a+bを余りグループに追加。
ansからaを引く。
以後、緩衝材グループからaが出てきた場合は一個スキップする。
以後、余りグループからbが出てきた場合は一個スキップする。
緩衝材グループのサイズはxのまま。

・aもbも緩衝材でなかった
a+bを余りグループに追加。
緩衝材グループの最大値を一つ余りグループに移動させる。
以後、緩衝材グループからa,bが出てきた場合は一個スキップする。
以後、余りグループからa,bが出てきた場合は一個スキップする。
緩衝材グループのサイズはx-1。


'''
