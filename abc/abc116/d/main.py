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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,k,*td0 = map(int,read().split())

it = iter(td0)
td = [[t,d] for t,d in zip(it,it)]
td.sort(key=lambda x:-1 * x[1])

eat = [0] * (n+1)
now = 0
val = 0
for i in range(k):
    t,d = td[i]
    now += d
    if(eat[t] == 0):
        val += 1
    eat[t] += 1

ans = now + val**2
l = k-1
for r in range(k,n):
    # print(r,now,val,ans)
    t,d = td[r]
    if(eat[t] != 0):
        continue
    while(l >= 0):
        tl,dl = td[l]
        l -= 1
        if(eat[tl] >= 2):
            now += d-dl
            val += 1
            eat[t] += 1
            ans = max(ans,now + val**2)
            break
    else:
        print(ans)
        exit()
    
print(ans)


'''
おいしさでソートして、
前からk個持っていく。
この時各ネタの食べた個数を覚えておく。
k+1個目については、新規ネタの時だけ食べる。
その代わり、2個以上食べたネタのうち最も安いものを捨てる。

'''