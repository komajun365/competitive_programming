n,a,b = map(int, input().split())

ans = 0
for i in range(1,n+1):
    i_num = (i//10000) + ((i//1000)%10) + ((i//100)%10) + ((i//10)%10) + (i%10)
    if (i_num >= a)&(i_num <= b):
        ans += i

print(ans)
# 
# i= 10000
# print(i//1000)
# print((i//100)%10)
# print((i//10)%10)
# print(i%10)
