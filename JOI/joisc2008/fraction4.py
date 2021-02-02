# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# https://www.ioi-jp.org/camp/2008/2008-sp-tasks/2008-sp_tr-day1_20.pdf
# 検討30分　実装8分 バグとり3分 でTLE

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

def main():
    """"ここに今までのコード"""
    from heapq import heappush,heappop,heapify
    from fractions import gcd

    m,k = map(int,input().split())

    hq = [(1/i, (1,i)) for i in range(2,m+1)]
    heapify(hq)

    tmp = 0
    for _ in range(k):
        if(not hq):
            print(-1)
            exit()
        tmp = heappop(hq)
        a,b = tmp[1]
        while(True):
            a += 1

            if(a==b):
                break
            if(gcd(a,b)==1):
                heappush(hq,(a/b, (a,b)))
                break
    print(' '.join(map(str,tmp[1])))

if __name__ == '__main__':
    main()






'''
方針
分子がiの既約分数の数　+ 分母がiの既約分数の数
→　1~mでiと素な数の数え上げ


1/iと1/j (j=i-1)の間にいくつ分数があるか？
i,j = (3,2)
2/5
3/2
3/8
4/9
4/10
4/11
5/11
5/12
5/13
5/14
6/13
6/17
7/15
7/16
:

kが小さいので、小さいほうから全部見ていく？
heapでいけそう！

(1/i,(1,i))を初期値としてpushしておく
(x,(y,z))をpopした時、
(?,(y+1,z))をpushする。
ただし、1以上にならないように注意。
→　約分の問題は？
　 gcdして1じゃなくなるまでチェックする？

m=6の場合
(1/6)
(1/5,5/6)
(1/4,2/5,5/6)
(1/3,2/5,3/4,5/6)
(1/2,2/5,2/3,3/4,5/6)
(2/5,2/3,3/4,5/6)
()

計算量は？
heapの作成：O(M)
heappop:O(logK)
heappush:O(?*loglogM+logK)
'''
