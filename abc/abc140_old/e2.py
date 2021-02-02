import heapq

n = int(input())
p = list(map(int, input().split()))

dic = [0] * n
for i in range(n):
    dic[p[i]-1] = i+1

ans = 0
big = {0,n+1}
big.add(dic[n-1])
for i in range(n-1,0,-1):
    i_no = dic[i-1]
    bigger = big & set(range(i_no+1,n+2,1))
    smaller = big & set(range(i_no-1,-1,-1))

    if len(bigger)==1:
        r1 = n+1
        r2 = n+1
    else:
        r1, r2 = heapq.nsmallest(2, bigger)
        # r1 = min(bigger)
        # bigger.discard(r1)
        # r2 = min(bigger)

    if len(smaller)==1:
        l1 = 0
        l2 = 0
    else:
        l1, r2 = heapq.nlargest(2, smaller)
        # l1 = max(smaller)
        # smaller.discard(l1)
        # l2 = max(smaller)

    ans += i*((r2-r1)*(i_no-l1)+(r1-i_no)*(l1-l2))

    big.add(i_no)

print(ans)










N = 8
P =[8 ,2 ,7 ,3 ,4 ,5 ,6 ,1]

# N = int(input())
# P = list(map(int, input().split()))

left_bigger  = [0] + [i for i in range(N+1)]
right_bigger = [i+1 for i in range(N+1)] + [N+1]

E = [(v, i+1) for i, v in enumerate(P)]
E
E.sort()
E

v,i = E[0]

l0=left_bigger[i]
l1=left_bigger[l0]
r0=right_bigger[i]
r1=right_bigger[r0]
l0,l1,r0,r1

left_bigger
right_bigger

left_bigger[r0]=l0
right_bigger[l0]=r0

left_bigger
right_bigger
