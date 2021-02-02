s = int(input())
nums = list(map(int, input().split()))

count = 0
flag = True
while(flag):
    div = 2**(count+1)
    if sum(map(lambda x: x%div, nums))==0:
        count += 1
    else:
        flag = False

print(count)
