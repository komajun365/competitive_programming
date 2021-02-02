from itertools import combinations
from collections import Counter
from collections import defaultdict

N, M = map(int, input().split())
L = list(map(lambda x: int(x)**2, input().split()))

counter = Counter(L)
candidates = defaultdict(float)
ans = 0

for x, y in combinations(L, 2):
    z1 = x + y
    z2 = abs(x - y)
    ans += counter.get(z1, 0)

    candidates[z1] += M
    if z2 != 0:
        candidates[z2] += M

for x in L:
    z = x / 2
    candidates[z] += M * (M - 1) // 2

if len(candidates) != 0:
    ans += max(candidates.values())

print(int(ans))
