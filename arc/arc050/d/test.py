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

def sa_naive(s):
    n = len(s)
    sa = list(range(n))
    sa.sort(key=lambda x: s[x:])
    return sa


def sa_doubling(s):
    # バグってるっぽい
    n = len(s)
    sa = list(range(n))
    rnk = s[::]
    tmp = [0] * n
    k = 1
    while k < n:
        def cmp(x):
            first = rnk[x] * n_plus
            second = -1 if (x + k >= n) else rnk[x + k]
            return first + second
        sa.sort(key=cmp)
        tmp[sa[0]] = 0
        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i - 1]] + (cmp(sa[i]) > cmp(sa[i - 1]))
        rnk, tmp = tmp, rnk
        k *= 2
    return sa

def sa_doubling(s):
    n = len(s)
    n_plus = n + 10
    sa = list(range(n))
    rnk = s[::]
    tmp = [0] * n
    k = 1
    while k < n:
        def cmp(x):
            first = rnk[x] * n_plus
            second = -1 if (x + k >= n) else rnk[x + k]
            return first + second
        sa.sort(key=cmp)
        tmp[sa[0]] = 0
        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i - 1]] + (cmp(sa[i]) > cmp(sa[i - 1]))
        rnk, tmp = tmp, rnk
        k *= 2
    return sa


def sa_is(s, upper):
    THRESHOLD_NAIVE = 20
    THRESHOLD_DOUBLING = 20

    n = len(s)
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        if s[0] < s[1]:
            return [0, 1]
        else:
            return [1, 0]

    if n < THRESHOLD_NAIVE:
        return sa_naive(s)
    elif n < THRESHOLD_DOUBLING:
        return sa_doubling(s)

    sa = [0] * n
    ls = [0] * n
    for i in range(n - 2, -1, -1):
        ls[i] = ls[i + 1] if s[i] == s[i + 1] else s[i] < s[i + 1]
    sum_l = [0] * (upper + 1)
    sum_s = [0] * (upper + 1)
    for i in range(n):
        if not ls[i]:
            sum_s[s[i]] += 1
        else:
            sum_l[s[i] + 1] += 1
    for i in range(upper):
        sum_s[i] += sum_l[i]
        if i < upper:
            sum_l[i + 1] += sum_s[i]

    def induce(lms: list):
        nonlocal sa, sum_s, sum_l
        sa = [-1] * n
        buf = sum_s[::]
        for d in lms:
            if d == n:
                continue
            sa[buf[s[d]]] = d
            buf[s[d]] += 1
        buf = sum_l[::]
        sa[buf[s[n - 1]]] = n - 1
        buf[s[n - 1]] += 1
        for i in range(n):
            v = sa[i]
            if v >= 1 and not ls[v - 1]:
                sa[buf[s[v - 1]]] = v - 1
                buf[s[v - 1]] += 1
        buf = sum_l[::]
        for i in range(n - 1, -1, -1):
            v = sa[i]
            if v >= 1 and ls[v - 1]:
                buf[s[v - 1] + 1] -= 1
                sa[buf[s[v - 1] + 1]] = v - 1

    lms_map = [-1] * (n + 1)
    m = 0
    for i in range(1, n):
        if not ls[i - 1] and ls[i]:
            lms_map[i] = m
            m += 1
    lms = []
    for i in range(1, n):
        if not ls[i - 1] and ls[i]:
            lms.append(i)

    induce(lms)

    if m:
        sorted_lms = []
        for v in sa:
            if lms_map[v] != -1:
                sorted_lms.append(v)
        rec_s = [0] * m
        rec_upper = 0
        rec_s[lms_map[sorted_lms[0]]] = 0
        for i in range(1, m):
            left, right = sorted_lms[i - 1:i + 1]
            end_l = lms[lms_map[left] + 1] if (lms_map[left] + 1 < m) else n
            end_r = lms[lms_map[right] + 1] if (lms_map[right] + 1 < m) else n
            same = True
            if end_l - left != end_r - right:
                same = False
            else:
                while left < end_l:
                    if s[left] != s[right]:
                        break
                    left += 1
                    right += 1
                if left == n:
                    same = False
                elif s[left] != s[right]:
                    same = False
            if not same:
                rec_upper += 1
            rec_s[lms_map[sorted_lms[i]]] = rec_upper

        rec_sa = sa_is(rec_s, rec_upper)

        for i in range(m):
            sorted_lms[i] = lms[rec_sa[i]]

        induce(sorted_lms)

    return sa


def suffix_array(s, upper: int = -1):
    n = len(s)
    if type(s) is list and upper >= 0:
        assert 0 <= min(s) and max(s) <= upper
        return sa_is(s, upper)

    elif type(s) is list and upper == -1:
        idx = list(range(n))
        idx.sort(key=lambda x: s[x])
        s2 = [0] * n
        now = 0
        for i in range(n):
            if i and s[idx[i - 1]] != s[idx[i]]:
                now += 1
            s2[idx[i]] = now
        return sa_is(s2, now)

    elif type(s) is str:
        s2 = [0] * n
        for i, si in enumerate(s):
            s2[i] = ord(si)
        return sa_is(s2, 255)

    else:
        print('type error')
        assert 0 == 1


def lcp_array(s, sa: list):
    n = len(s)
    assert n >= 1
    if type(s) is str:
        s2 = [0] * n
        for i, si in enumerate(s):
            s2[i] = ord(si)
        s = s2

    rnk = [0] * n
    for i, sai in enumerate(sa):
        rnk[sai] = i
    lcp = [0] * (n - 1)
    h = 0
    for i in range(n):
        if h > 0:
            h -= 1
        if rnk[i] == 0:
            continue
        j = sa[rnk[i] - 1]
        while j + h < n and i + h < n:
            if s[j + h] != s[i + h]:
                break
            h += 1
        lcp[rnk[i] - 1] = h
    return lcp

def solve(n,s):
    # n = int(input())
    # s = input()

    sa = suffix_array(s)
    lcp = lcp_array(s,sa)

    sa_rev = [0] * n
    for i in range(n):
        sa_rev[sa[i]] = i

    ans = []
    stack = []
    use = [0] * n
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            left = sa[j-1]
            right = sa[j]
            len_l = n - left
            if lcp[j-1] != len_l:
                break
            r2 = right + len_l
            if sa_rev[right] < sa_rev[r2]:
                ans.append(left + 1)
                use[left] = 1
            j += 1
        for k in range(j-1,i-1,-1):
            if use[sa[k]] == 0:
                ans.append(sa[k]+1)
        # print(ans)
        # print(use)
        i = j

    # print('\n'.join(map(str,ans)))
    return ans

def solve_simple(n,s):
    ss = []
    for i in range(n):
        ss.append(s[i:])
    links = [set() for _ in range(n)]
    deg_in = [0] * n
    for i in range(n-1):
        for j in range(i+1, n):
            s1 = ss[i] + ss[j]
            s2 = ss[j] + ss[i]
            # print(i,j,s1,s2,s1<=s2)
            if s1 <= s2:
                links[i].add(j)
                deg_in[j] += 1
            else:
                links[j].add(i)
                deg_in[i] += 1
    
    # print(deg_in)
    res = [0] * n
    for i in range(n):
        res[deg_in[i]] = i+1
    
    return res

# print(solve_simple(11,'abaabcabaab'))

from random import randint
for _ in range(1000):
    n = randint(1,10)
    s = ''
    for _ in range(n):
        s += chr(ord('a') + randint(0,25))
    
    res1 = solve(n,s)
    res2 = solve_simple(n,s)
    if res1 != res2:
        print(n,s)
        print(res1)
        print(res2)
        exit()




# print(sa)
# print(lcp)
# print(sa_rev)