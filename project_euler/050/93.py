# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import itertools

def calc(a,b):
    res = []
    for i in a:
        for j in b:
            res = res + [i+j,i-j,i*j,i/j]
    return res

def calc2(a,b,c,d):
    check = [0] * 100
    it = itertools.permutations((a,b,c,d))
    for (e,f,g,h) in it:
        for x in calc([e],[f]):
            for y in calc([x],calc([g],[h])):
                if(y==int(y))&(0<y<100):
                    check[int(y)] = 1
            for y in calc(calc([x],[g]),[h]):
                if(y==int(y))&(0<y<100):
                    check[int(y)] = 1

    for i in range(1,100):
        if(check[i] == 0):
            break

    return i-1

ans = (1,2,3,4)
ans_max = 0

for a,b,c,d in itertools.combinations(range(1,10),4):
    tmp = calc2(a,b,c,d)
    if(ans_max < tmp):
        ans = (a,b,c,d)
        ans_max = tmp

print(ans)
print(ans_max)


'''
calc(a,b)
a+b
a-b
a*c
a/d

[[a,b][c,d]]
[[[a,b],c],d]
並び替えてやってく

1このa,b,c,dで24パターン
64回のcalc

'''
