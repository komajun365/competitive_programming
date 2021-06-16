# oj t -c "python main.py" -d "./tests/" 

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
f = open('../../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
import time
from heapq import heappop, heappush
import random
import math

def initialize(n,xyr):
    res = []
    it = iter(xyr)
    for x,y,_ in zip(it,it,it):
        res.append([x,y,x+1,y+1])
    return res

def initialize_otw(n,xyr,res,p0,p1):
    it = iter(xyr)
    res2 = []
    for x,y,_, i in zip(it,it,it, range(n)):
        a0,b0,c0,d0 = x,y,x+1,y+1
        a,b,c,d = res[i]
#         print(a,b,c,d,a0,b0,c0,d0)
        a = a0 - int((a0-a) * (random.random() * (p1-p0) +p0))
        b = b0 - int((b0-b) * (random.random() * (p1-p0) +p0))
        c = c0 + int((c-c0) * (random.random() * (p1-p0) +p0))
        d = d0 + int((d-d0) * (random.random() * (p1-p0) +p0))
#         print(a,b,c,d,a0,b0,c0,d0)
        res2.append([a,b,c,d])
    return res2

def initialize_otw2(n,xyr,res,p0,p1):
    it = iter(xyr)
    res2 = []
    for x,y,_, i in zip(it,it,it, range(n)):
        a0,b0,c0,d0 = x,y,x+1,y+1
        a,b,c,d = res[i]
        if random.random() > random.random()*0.6 + 0.4:
            res2.append([a,b,c,d])
            continue
#         print(a,b,c,d,a0,b0,c0,d0)
        a = a0 - int((a0-a) * (random.random() * (p1-p0) +p0))
        b = b0 - int((b0-b) * (random.random() * (p1-p0) +p0))
        c = c0 + int((c-c0) * (random.random() * (p1-p0) +p0))
        d = d0 + int((d-d0) * (random.random() * (p1-p0) +p0))
#         print(a,b,c,d,a0,b0,c0,d0)
        res2.append([a,b,c,d])
    return res2

def able_extend(x, r, ans):
    # O(4n)
    n = len(r)
    a,b,c,d = ans[x]
    ri = r[x]
    able_x = ri//(d-b) -(c-a)
    able_y = ri//(c-a) -(d-b)

    res = [min(a, able_x),
           min(b, able_y),
           min(10000-c, able_x),
           min(10000-d, able_y)] # up,left,down,right
    for i in range(n):
        if i == x:
            continue
        ai,bi,ci,di = ans[i]
        # up
        if b < di and bi < d and ci <= a:
            res[0] = min(res[0], a - ci)
        # down
        if b < di and bi < d and c <= ai:
            res[2] = min(res[2], ai - c)
        # left
        if a < ci and ai < c and di <= b:
            res[1] = min(res[1], b - di)
        # right
        if a < ci and ai < c and d <= bi:
            res[3] = min(res[3], bi - d)
    max_num = max(res)
    if max_num <= 0:
        return res,-1
    start = random.randint(-3,0)
    for i in range(start, start+4):
        if res[i] == max_num:
            return res,i%4


def eval_extend(x, r, ans, cyc, under):
    a,b,c,d = ans[x]
    ri = r[x]
    si = (c-a) * (d-b)
    point = 1 - (1 - min(ri,si)/max(ri,si))**2
    rem_point = 1 - point
    rem_area = max(0, ri-si)
        
    if rem_area == 0:
        return 0
    # if cyc > 15:
    #     return (1 + random.random())* (cyc-under[x]+1)**3
    # else:
    #     return (1 + random.random())

    if cyc > 8:
        return (-1 * rem_point / rem_area)* (under[x]+1)**5
    else:
        return (-1 * rem_point / rem_area)

    # if cyc > 15:
    #     return (1 / (-1 * rem_point / rem_area))* (under[x]+1)**3
    # else:
    #     return (1 / (-1 * rem_point / rem_area))

    # if cyc > 30:
    #     if cyc % 3 == 0:
    #         return 1 + random.random() * (cyc-under[x]+1)**3
    #     if cyc % 3 == 1:
    #         return (-1 * rem_point / rem_area)* (under[x]+1)**3
    #     else:
    #         return (1 / (-1 * rem_point / rem_area))* (under[x]+1)**3
    # if cyc % 3 == 0:
    #     return 1 + random.random()
    # if cyc % 3 == 1:
    #     return -1 * rem_point / rem_area
    # else:
    #     return 1 / (-1 * rem_point / rem_area)


def calc_score(r,ans, under):
    n = len(r)
    res = 0
    for i in range(n):
        ri  = r[i]
        a,b,c,d = ans[i]
        si = (c-a) * (d-b)
        p = 1 - (1 - min(ri,si)/max(ri,si))**2
        res += p
        if p < 0.7:
            under[i] += 1
    return res, under

def search_all(n,xyr,r,under,cyc,start,TIME_LIMIT):
    ans = initialize(n,xyr)
    ex_cnt = [0] * n
    eval_ex = []
    for i in range(n):
        eval_score = eval_extend(i, r, ans, cyc, under)
        if eval_score != 0:
            heappush(eval_ex, (eval_score, i))

    iter_cnt = 0
    pr = []
    while time.time() - start < TIME_LIMIT and eval_ex:
        iter_cnt += 1

        _,i = heappop(eval_ex)
        able_ex, idx = able_extend(i, r, ans)
        if idx == -1:
            continue

        if ex_cnt[i] < 20:
            idx = random.randint(0,3)
            ex_width = able_ex[idx]**0.5
            rand = random.random() * 0.5 + 1
            ex_width = math.ceil(ex_width * rand)
        elif ex_cnt[i] < 50:
            ex_width = able_ex[idx]**0.8
            rand = random.random() * 0.5 + 1
            ex_width = math.ceil(ex_width * rand)
        elif ex_cnt[i] < 60:
            rand = random.random() * 0.2 + 0.1 * min(8,(ex_cnt[i]-20)//4)
            ex_width = math.ceil(able_ex[idx] * rand)
        else:
            ex_width = math.ceil(able_ex[idx] * 0.1 + 0.9)

        ex_width = min(ex_width, able_ex[idx])
        # ex_width = max(ex_width, 1)
        if idx < 2:
            ans[i][idx] -= ex_width
        else:
            ans[i][idx] += ex_width
        eval_score =  eval_extend(i, r, ans, cyc, under)
        if eval_score == 0:
            continue
        ex_cnt[i] += 1
        heappush(eval_ex, (eval_score, i))

        pr.append((eval_score, i, idx, able_ex[idx], ex_width))

        # if iter_cnt % 300 == 0:
        #     point,_ = calc_score(r,ans, under)
        #     print(cyc,iter_cnt,point)
    return ans,iter_cnt

def search_on_the_way(n,xyr,r,under,cyc,start,TIME_LIMIT,res,p0,p1):
    ans = initialize_otw2(n,xyr,res,p0,p1)
    ex_cnt = [0] * n
    eval_ex = []
    for i in range(n):
        eval_score = eval_extend(i, r, ans, cyc, under)
        if eval_score != 0:
            heappush(eval_ex, (eval_score, i))

    iter_cnt = 0
    pr = []
    while time.time() - start < TIME_LIMIT and eval_ex:
        iter_cnt += 1

        _,i = heappop(eval_ex)
        able_ex, idx = able_extend(i, r, ans)
        if idx == -1:
            continue

        if ex_cnt[i] < 10:
            idx = random.randint(0,3)
            ex_width = able_ex[idx]**0.5
            rand = random.random() * 0.5 + 1
            ex_width = math.ceil(ex_width * rand)
        elif ex_cnt[i] < 25:
            ex_width = able_ex[idx]**0.8
            rand = random.random() * 0.5 + 1
            ex_width = math.ceil(ex_width * rand)
        elif ex_cnt[i] < 35:
            rand = random.random() * 0.2 + 0.1 * min(8,(ex_cnt[i]-20)//4)
            ex_width = math.ceil(able_ex[idx] * rand)
        else:
            ex_width = math.ceil(able_ex[idx] * 0.1 + 0.9)

        ex_width = min(ex_width, able_ex[idx])
        # ex_width = max(ex_width, 1)
        if idx < 2:
            ans[i][idx] -= ex_width
        else:
            ans[i][idx] += ex_width
        eval_score =  eval_extend(i, r, ans, cyc, under)
        if eval_score == 0:
            continue
        ex_cnt[i] += 1
        heappush(eval_ex, (eval_score, i))

        pr.append((eval_score, i, idx, able_ex[idx], ex_width))

        # if iter_cnt % 300 == 0:
        #     point,_ = calc_score(r,ans, under)
        #     print(cyc,iter_cnt,point)
    return ans,iter_cnt

def main(*args): 
    start = time.time()
    TIME_LIMIT = 10
    random.seed(42)
    
    if len(args) == 0:
        n,*xyr = map(int,read().split())
    else:
        n = args[0]
        xyr = args[1]
    r = xyr[2::3]
    res = []
    res_p = 0
    cyc = 0
    under = [0] * n
    
    while time.time() - start < TIME_LIMIT:
        if cyc < 50:
            ans,iter_cnt = search_all(n,xyr,r,under,cyc,start,TIME_LIMIT)
        elif cyc < 100:
            ans,iter_cnt = search_on_the_way(n,xyr,r,under,cyc,start,TIME_LIMIT,res,0.1,0.7)
        else:
            ans,iter_cnt = search_on_the_way(n,xyr,r,under,cyc,start,TIME_LIMIT,res,0.3,0.5)
        point,under = calc_score(r,ans, under)
        cyc += 1
        if cyc % 10 == 0:
            print(cyc,res_p)

        if res_p < point:
            res,ans = ans,res
            res_p = point
    
    # print(ex_cnt)
    print('\n'.join(map(lambda x: ' '.join(map(str,x)), res)))
    print(res_p)
    print(cyc)
    # print(under)
    
    # visualize(r, res, xyr)
          
if __name__ == "__main__":
    main()