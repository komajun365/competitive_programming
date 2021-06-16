# https://qiita.com/Kentaro_okumura/items/5b95b767a2e691cd5482

# 二分木
import bisect

# 再帰関数の上限解除
import sys
sys.setrecursionlimit(10**9)

# キュー
from collections import deque

# ヒープキュー（最小値・最大値の取得）
from heapq import heappop,heappush

# 最大公約数
# from fractions import gcd
from math import gcd

# deepcopy
from copy import deepcopy

# defaultdict
from collections import defaultdict
d = defaultdict(int)

#　順列など
# https://note.nkmk.me/python-math-factorial-permutations-combinations/
import itertools

# 再帰メモ化
from functools import lru_cache
@lru_cache(maxsize=10**9)

# 
if __name__ == "__main__":
    main()