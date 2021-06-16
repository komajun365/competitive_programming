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

def main():
    import sys
    read = sys.stdin.buffer.read

    n,*data = map(int,read().split())
    VW = tuple(data[:2*n])
    q = data[2*n]
    vL = data[2*n+1:]

    d = n.bit_length()
    d2 = min(10,d)
    max_L = max([l for l in vL[1::2]]) + 1

    dp = [0] * (max_L * 2**d2)
    for i in range(1,min(2**d2,n+1)):
        vi,wi = VW[(i-1)*2:i*2]    
        for j in range(max_L):
            before = (i//2)*max_L+j
            after = i*max_L+j
            if j < wi:
                dp[after] = dp[before]
            else:
                dp[after] = max(dp[after-1], dp[before-wi] + vi, dp[before])

    ans = []
    it = iter(vL)
    for v,L in zip(it,it):
        dv = v.bit_length()
        res = 0
        if dv <= d2:
            res = dp[v*max_L + L]
            ans.append(res)
            continue
        
        x = []
        i = v
        while i >= 2**d2:
            V,W = VW[(i-1)*2:i*2]
            x.append([V,W])
            i //= 2
        
        vs = [0]
        ws = [0]
        iml = i*max_L+L
        res = dp[iml]
        for vi,wi in x:
            l = len(vs)
            for j in range(l):
                vj = vs[j] + vi
                wj = ws[j] + wi
                if wj <= L:
                    res = max(res, dp[iml-wj] + vj)
                    vs.append(vj)
                    ws.append(wj)
        
        ans.append(res)

    print('\n'.join(map(str,ans)))

if __name__ == "__main__":
    main()


# import sys
# read = sys.stdin.buffer.read

# n,*data = map(int,read().split())
# VW = tuple(data[:2*n])
# q = data[2*n]
# vL = data[2*n+1:]

# d = n.bit_length()
# d2 = d//2
# max_L = max([l for l in vL[1::2]]) + 1

# dp = [0] * (max_L * 2**d2)
# for i in range(1,2**d2):
#     vi,wi = VW[(i-1)*2:i*2]    
#     for j in range(max_L):
#         before = (i//2)*max_L+j
#         after = i*max_L+j
#         if j < wi:
#             dp[after] = dp[before]
#         else:
#             dp[after] = max(dp[after-1], dp[before-wi] + vi, dp[before])

# ans = []
# it = iter(vL)
# for v,L in zip(it,it):
#     dv = v.bit_length()
#     res = 0
#     if dv <= d2:
#         res = dp[v*max_L + L]
#         ans.append(res)
#         continue
    
#     x = []
#     i = v
#     while i >= 2**d2:
#         V,W = VW[(i-1)*2:i*2]
#         x.append([V,W])
#         i //= 2
    
#     vs = [0]
#     ws = [0]
#     iml = i*max_L+L
#     res = dp[iml]
#     for vi,wi in x:
#         l = len(vs)
#         for j in range(l):
#             vj = vs[j] + vi
#             wj = ws[j] + wi
#             if wj <= L:
#                 res = max(res, dp[iml-wj] + vj)
#                 vs.append(vj)
#                 ws.append(wj)
    
#     ans.append(res)

# print('\n'.join(map(str,ans)))

# print(dp[3])
    


# def make_vw(x,L):
#     l = len(x)
#     res = [[0,0]]
#     for i in range(l):
#         l2 = len(res)
#         vi,wi = x[i]
#         for j in range(l2):
#             vj,wj = res[j]
#             if wi + wj <= L:
#                 res.append([vi+vj,wi+wj])

#     return res


# def excute_query(v,L):
#     dv = v.bit_length()
#     res = 0
#     if dv <= d2:
#         res = dp[v][L]
#         return res
    
#     x = []
#     i = v
#     while i >= 2**d2:
#         V,W = VW[(i-1)*2:i*2]
#         x.append([V,W])
#         i //= 2
#     under = make_vw(x,L)
#     for vu,wu in under:
#         res = max(res, dp[i][L-wu] + vu)
#     return res

# ans = []
# it = iter(vL)
# for v,L in zip(it,it):
#     ans.append(excute_query(v,L))

# print('\n'.join(map(str,ans)))














