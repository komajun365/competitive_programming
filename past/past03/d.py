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

n = int(input())
s = [input() for _ in range(5)]

st = list(zip(*s))

samp = ['.###..#..###.###.#.#.###.###.###.###.###.',
        '.#.#.##....#...#.#.#.#...#.....#.#.#.#.#.',
        '.#.#..#..###.###.###.###.###...#.###.###.',
        '.#.#..#..#.....#...#...#.#.#...#.#.#...#.',
        '.###.###.###.###...#.###.###...#.###.###.']

def check(x):
    for i in range(10):
        for j in range(5):
            cnt = 0
            for k in [1,2,3]:
                cnt += (samp[j][i*4+k] == x[j][k])
            if(cnt != 3):
                break
        else:
            return str(i)

ans = ''
for i in range(n):
    x = st[i*4:(i+1)*4]
    x = list(zip(*x))
    ans = ans + check(x)
print(ans)
