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

ans = []
for i in range(1<<n):
    cnt = 0
    left = 0
    tmp = ''
    for j in range(n):
        if (i >> j) & 1:
            cnt += 1
            left += 1
            tmp += ')'
        else:
            left -= 1
            tmp += '('
        if left < 0:
            break
    else:
        if cnt*2 == n:
            ans.append(tmp[::-1])

print('\n'.join(ans))

# ten = '''((((()))))
# (((()())))
# (((())()))
# (((()))())
# (((())))()
# ((()(())))
# ((()()()))
# ((()())())
# ((()()))()
# ((())(()))
# ((())()())
# ((())())()
# ((()))(())
# ((()))()()
# (()((())))
# (()(()()))
# (()(())())
# (()(()))()
# (()()(()))
# (()()()())
# (()()())()
# (()())(())
# (()())()()
# (())((()))
# (())(()())
# (())(())()
# (())()(())
# (())()()()
# ()(((())))
# ()((()()))
# ()((())())
# ()((()))()
# ()(()(()))
# ()(()()())
# ()(()())()
# ()(())(())
# ()(())()()
# ()()((()))
# ()()(()())
# ()()(())()
# ()()()(())
# ()()()()()
# '''
# ten= ten.split()
# for 
