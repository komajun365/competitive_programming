# input
s = input()
n = int(input())
n,m = map(int, input().split())
a = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]


import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,k = map(int, readline().split())
a = [list(map(int, i.split())) for i in readlines() ]

##############################

# output
print(' '.join([str(x) for x in ans]))

for x in ans:
    print(x)

for i in range(len(ans)):
    print(' '.join([str(x) for x in ans[i]]))
