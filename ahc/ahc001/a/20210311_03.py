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

def initialize(n,xy,r):
    res = []
    it = iter(xy)
    score_i = [0] * n
    for i in range(n):
        x,y = xy[i]
        ri = r[i]
        res.append([x,y,x+1,y+1])
        si = 1
        score_i[i] = 1 - (1 - min(ri,si)/max(ri,si))**2
        
    return res,score_i

def initialize_on_the_way(n,xy,r,res0,p0,p1):
    res = []
    score_i = [0] * n
    for i in range(n):
        x,y = xy[i]
        ri = r[i]
        a0,b0,c0,d0 = x,y,x+1,y+1
        a,b,c,d = res0[i]

        if random.random() > 0.7:
            res.append([a,b,c,d])
            continue
        a = a0 - int((a0-a) * (random.random() * (p1-p0) +p0))
        b = b0 - int((b0-b) * (random.random() * (p1-p0) +p0))
        c = c0 + int((c-c0) * (random.random() * (p1-p0) +p0))
        d = d0 + int((d-d0) * (random.random() * (p1-p0) +p0))
        res.append([a,b,c,d])
        si = (c-a) * (d-b)
        score_i[i] = 1 - (1 - min(ri,si)/max(ri,si))**2
    return res,score_i

def able_extend(x, r, res):
    # O(4n)
    n = len(r)
    a,b,c,d = res[x]
    ri = r[x]
    able_x = ri//(d-b) -(c-a)
    able_y = ri//(c-a) -(d-b)

    able_ex = [min(a, able_x),
           min(b, able_y),
           min(10000-c, able_x),
           min(10000-d, able_y)] # up,left,down,right
    for i in range(n):
        if i == x:
            continue
        ai,bi,ci,di = res[i]
        # up
        if b < di and bi < d and ci <= a:
            able_ex[0] = min(able_ex[0], a - ci)
        # down
        elif b < di and bi < d and c <= ai:
            able_ex[2] = min(able_ex[2], ai - c)
        # left
        elif a < ci and ai < c and di <= b:
            able_ex[1] = min(able_ex[1], b - di)
        # right
        elif a < ci and ai < c and d <= bi:
            able_ex[3] = min(able_ex[3], bi - d)
    max_num = max(able_ex)
    if max_num <= 0:
        return able_ex,-1
    start_i = random.randint(-3,0)
    for i in range(start_i, start_i+4):
        if able_ex[i] == max_num:
            return able_ex,i%4

def calc_score_x(i, r, res):
    a,b,c,d = res[i]
    si = (c-a) * (d-b)
    ri = r[i]
    return 1 - (1 - min(ri,si)/max(ri,si))**2

def eval_extend(i, xy, r, res, cyc, under):
    a,b,c,d = res[i]
    ri = r[i]
    si = (c-a) * (d-b)
    point = 1 - (1 - min(ri,si)/max(ri,si))**2
    rem_point = 1 - point
    rem_area = max(0, ri-si)
        
    if rem_area == 0:
        return 0

    if cyc > 8:
        return (-1 * rem_point / rem_area)* (under[i]+1)**5
    else:
        return (-1 * rem_point / rem_area)

def eval_extend_random(i, xy, r, res, cyc, under):
    return -1 * random.random() *  (under[i]+1)**5

def search_on_the_way(n,xy,r,under,cyc,res0,p0,p1):
    # 初期化
    res, score_i = initialize_on_the_way(n,xy,r,res0,p0,p1)
    score = sum(score_i)
    ex_cnt = [0] * n
    
    # 更新順位heapqueの作成
    eval_ex = []
    for i in range(n):
        eval_score = eval_extend(i, xy, r, res, cyc, under)
#         eval_score = eval_extend_random(i, xy, r, res, cyc, under)

        if eval_score != 0:
            heappush(eval_ex, (eval_score, i))
    
    iter_cnt = 0
    
    while eval_ex:
        iter_cnt += 1
        # 時間確認
        if iter_cnt % 500 == 0:
            if time.time() - start > TIME_LIMIT:
                break
        
        # 伸ばすbox、辺、長さの決定
        _,i = heappop(eval_ex)
        able_ex, idx = able_extend(i, r, res)
        if idx == -1:
            # 伸ばせる辺がない場合
            continue
        
        # ここは要調整
        if ex_cnt[i] < 10:
            idx = random.randint(0,3)
            ex_width = able_ex[idx]**0.5
            rand = random.random() + 0.5
            ex_width = math.ceil(ex_width * rand)
        elif ex_cnt[i] < 15:
            ex_width = able_ex[idx]**0.8
            rand = random.random() + 1
            ex_width = math.ceil(ex_width * rand)
        elif ex_cnt[i] < 20:
            rand = random.random() * 0.2 + 0.1 * min(8,(ex_cnt[i]-4)//2)
            ex_width = math.ceil(able_ex[idx] * rand)
        else:
            rand = random.random() * 0.1 + 0.9
            ex_width = math.ceil(able_ex[idx] * rand )
        
        # 最大値を超えないように調整
        ex_width = min(ex_width, able_ex[idx])
        
        # 値の更新
        if idx < 2:
            res[i][idx] -= ex_width
        else:
            res[i][idx] += ex_width
        new_score = calc_score_x(i,r,res)
        score += new_score - score_i[i]
        score_i[i] = new_score
        
        # 更新の必要のないboxはスキップ
        if score_i[i] > 0.99:
            continue
        
        # 更新順位heapqueの更新
        eval_score = eval_extend(i, xy, r, res, cyc, under)
#         eval_score = eval_extend_random(i, xy, r, res, cyc, under)
        if eval_score != 0:
            heappush(eval_ex, (eval_score, i))
        
        ex_cnt[i] += 1
        
        # デバッグ用出力
        if DEBUG_SEARCH:
            if iter_cnt % 500 == 0:
                print(cyc,iter_cnt,score)
    
    return res, score, score_i, iter_cnt

def search_all(n,xy,r,under,cyc):
    # 初期化
    res, score_i = initialize(n,xy,r)
    score = sum(score_i)
    ex_cnt = [0] * n
    
    # 更新順位heapqueの作成
    eval_ex = []
    for i in range(n):
        eval_score = eval_extend(i, xy, r, res, cyc, under)
#         eval_score = eval_extend_random(i, xy, r, res, cyc, under)

        if eval_score != 0:
            heappush(eval_ex, (eval_score, i))
    
    iter_cnt = 0
    
    while eval_ex:
        iter_cnt += 1
        # 時間確認
        if iter_cnt % 500 == 0:
            if time.time() - start > TIME_LIMIT:
                break
        
        # 伸ばすbox、辺、長さの決定
        _,i = heappop(eval_ex)
        able_ex, idx = able_extend(i, r, res)
        if idx == -1:
            # 伸ばせる辺がない場合
            continue
        
        # ここは要調整
        if ex_cnt[i] < 20:
            idx = random.randint(0,3)
            ex_width = able_ex[idx]**0.5
            rand = random.random() + 0.5
            ex_width = math.ceil(ex_width * rand)
        elif ex_cnt[i] < 40:
            ex_width = able_ex[idx]**0.8
            rand = random.random() + 1
            ex_width = math.ceil(ex_width * rand)
        elif ex_cnt[i] < 60:
            rand = random.random() * 0.2 + 0.1 * min(8,(ex_cnt[i]-28)//4)
            ex_width = math.ceil(able_ex[idx] * rand)
        else:
            rand = random.random() * 0.1 + 0.9
            ex_width = math.ceil(able_ex[idx] * rand )
        
        # 最大値を超えないように調整
        ex_width = min(ex_width, able_ex[idx])
        
        # 値の更新
        if idx < 2:
            res[i][idx] -= ex_width
        else:
            res[i][idx] += ex_width
        new_score = calc_score_x(i,r,res)
        score += new_score - score_i[i]
        score_i[i] = new_score
        
        # 更新の必要のないboxはスキップ
        if score_i[i] > 0.99:
            continue
        
        # 更新順位heapqueの更新
        eval_score = eval_extend(i, xy, r, res, cyc, under)
#         eval_score = eval_extend_random(i, xy, r, res, cyc, under)
        if eval_score != 0:
            heappush(eval_ex, (eval_score, i))
        
        ex_cnt[i] += 1
        
        # デバッグ用出力
        if DEBUG_SEARCH:
            if iter_cnt % 500 == 0:
                print(cyc,iter_cnt,score)
    
    return res, score, score_i, iter_cnt

def main(*args):
    # 入力
    if len(args) == 0:
        n,*xyr = map(int,read().split())
    else:
        n = args[0]
        xyr = args[1]
    
    # 変数準備
    xy = []
    r = []
    it = iter(xyr)
    for xi,yi,ri in zip(it,it,it):
        xy.append([xi,yi])
        r.append(ri)
    res = []
    res_score = 0
    cyc = 0
    under = [0] * n
    
    while time.time() - start < TIME_LIMIT:
        # 出力作成
        if cyc < 10:
            res2, score, score_i, iter_cnt = search_all(n,xy,r,under,cyc)
        elif time.time() - start < 4.4:
            res2, score, score_i, iter_cnt = search_on_the_way(n,xy,r,under,cyc,res,0.1,0.7)
        else:
            res2, score, score_i, iter_cnt = search_on_the_way(n,xy,r,under,cyc,res,0.3,0.5)
                
        # 更新
        if score > res_score:
            res,res2 = res2,res
            res_score = score
        for i in range(n):
            if score_i[i] < UNDER:
                under[i] += 1
        
        # デバッグ用出力
        if DEBUG:
            pass
        
        cyc += 1
        
    # 解答出力
    print('\n'.join(map(lambda x: ' '.join(map(str,x)), res)))
    
    # デバッグ用出力
    if DEBUG:
        print(res_score / n)
        print(cyc)
        print(under)
        # visualize(res, xy, r)

    return [res_score / n, cyc]


####################################

#定数など
start = time.time()
TIME_LIMIT = 4.7
random.seed(42)

UNDER = 0.8
DEBUG = True
DEBUG_SEARCH = False


if __name__ == "__main__":
    main()