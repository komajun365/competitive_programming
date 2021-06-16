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

n,d1,x = map(int,input().split())

tot = d1*2*n + (2*n-1)*(2*n)//2*x
ave = tot/(n*2)

ans = 0
for i in range(n):
    ans += ave
    ave *= (n-i+1) / (n-i)

print(ans)



# p_now = 1
# prob = [0] * n
# prob[0] = 0.5
# for i in range(1,n):
#     p_now *= (i*2-1)/(i*2)
#     prob[i] = 0.5 * p_now * (1/(i+1))
#     prob[i-1] -= prob[i] * (n-i) / (n-i+1)

# ans = 0
# for i in range(n):
#     ans += ave * (i*2+1) * (n-i) * 2 * prob[i]
#     # print(i, ans)

# print(ans)
# print(prob)


# left = d1*n + n*(n-1)*x 
# right = d1*n + n*n*x
# tot = left + right

# ml = d1 * 3 + ((2*n-1) + (2*n-2))*x
# mr = d1 * 3 + x + (2*n-1) * x

# ans = tot * 0.5
# print(0,ans,left,right,ml,mr)


# prob = 1
# for i in range(1,n):
#     left += tot - ml 
#     right += tot - mr
#     ml += d1 * 4 + ((2*n-i*2-1) + (2*n-i*2-2)) * x + (i*2-1 + i*2) * x
#     mr += d1 * 4 + ((i*2+1) + (i*2+2)) * x + ((2*n-i*2) + (2*n-i*2-1)) * x

#     ans += (right+left) * prob * 0.25 * (1/(i+1)) * (1/i)
#     prob *= (i*2-1)/(i*2)
#     print(i,ans,left,right,ml,mr)

# print(ans)

'''
 1 3
0 2 4

・1 -> 2
2 + 1

・1 -> 4
1

・1 -> 0
2 + 2

・3 -> 0
1

・3 -> 2
2 + 1

・3 -> 4
2 + 2

4,4,4,4,4,4

 4,4,4,4
 12,4,4,4
 4,12,4,4
 4,4,12,4
 4,4,4,12
 4,4,4,4



16/6,16/6,16/6,16/6

8/6


'''