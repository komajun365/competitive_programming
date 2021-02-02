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


'''
最後の石を取ったものが勝者。
それがx手目だとすると、
x-1手目の人は、a個取って、2a個以下の個数になってしまったということ。
aを大きく取り過ぎるとそりゃそうやろ、って感じなので、
全部とれない限りはa=1である。
以降、残りの3分の１以上持っていくような手は考えないことにする。

残り3個の状態で、最大2個しかとれなければ必敗。
ということはつまり、残り4個の状態で1個だけ取れば勝ち。

残り5個は負け
残り6個は勝ち
残り7個は勝ち
8は負け
9は勝ち
10勝ち
11lose
12win
13lose
14lose
15win
16win
17win
：
：

残りの3分の１個未満の石を取っていくnimだと思えばよさそう。




f(n,b) := 今n個で、前回b個取られた時の勝敗（1,0）とすると、
・n<=2bなら勝ち
・f(n-i,i)が全て勝ちなら負け
・それ以外は勝ち



'''
