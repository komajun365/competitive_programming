n,k,q = map(int, input().split())

point_list = [0]*n

for i in range(q):
    a = int(input()) -1
    point_list[a] = point_list[a] +1

for p in point_list:
    if p > q-k:
        print('Yes')
    else:
        print('No')
