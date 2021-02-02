n = int(input())
v_list = map(int,input().split())

v_list2 = sorted(v_list)

ans = v_list2[0]
for i in range(1,n):
    ans = (ans + v_list2[i])/2

print(ans)
