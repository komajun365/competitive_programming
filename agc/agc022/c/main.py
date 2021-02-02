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

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

goal = [1<<ai for ai in a]
start = [1<<bi for bi in b]

mask = (1<<51)-1

def get_max(start,goal):
    s = start[::]
    g = goal[::]
    for k in range(51):
        check = True
        for i in range(n):
            si = s[i]
            gi = g[i]
            if(k != 0):
                base = si & ((1<<k) -1)
                if(base != 0):
                    for j in range(k,51,k):
                        si |= base << j
            si &= mask
            if(si & gi) == 0:
                check = False
            s[i] = si
        if check:
            return k
    return -1

ans = 0
for _ in range(60):
    k_max = get_max(start,goal)
    if(k_max==0):
        print(ans)
        exit()
    if(k_max==-1):
        print(-1)
        exit()
    
    ans += 2**k_max
    for i in range(n):
        mask_k = (1<<k_max) -1
        add = 0
        for j in range(0,51,k_max):
            add |= (goal[i] >> j) & mask_k
        goal[i] |= add
    # print(k_max)
    # print(goal)
    # print(start)

    



            
                






'''
kの処理は大きいものから小さいものへと順番にやっていくと考えていい。
同じ数字を2回選ぶ理由もない。

コストの形を考えると、とにかく最大のkを小さくしたい。

x --(%k)->  y
という作業を逆から考える。
yから考えてxの候補は、
y,y+k,y+2k,...
である。
(ただし、y<k)

kを1から増やしていくと、
元の値から到達できる数値がわかる。
最初に全ての数値が到達できたとき、kを採用すればいいときまる。

この処理をbitでうまくやる、かつbitの処理オーダーはO(1）とみなすとして、
N*NlogN = O(1.5*10**4)

最大値を決めた後は、k-1までで使う必要のある最大値をまた2から求めていけばいい。

'''