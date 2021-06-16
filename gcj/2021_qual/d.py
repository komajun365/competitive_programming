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
# f = open('../../input.txt', 'r')
# sys.stdin = f

t,n,q = map(int,input().split())

def solve(n):
    print('1 2 3', flush=True)
    res = input()
    if res == '1':
        nums = [2,1,3]
    elif res == '2':
        nums = [1,2,3]
    else:
        nums = [1,3,2]
    
    for i in range(4,n+1):
        # print(*nums)

        m = len(nums)
        l = 0
        r = m-1
        while r-l > 1:
            cnt = r-l+1
            mid1 = l + cnt//3
            mid2 = l + (cnt*2)//3
            # print('check:',cnt,mid1,mid2)
            print('{} {} {}'.format(i,nums[mid1],nums[mid2]), flush=True)
            res = int(input())
            if res == i:
                l = mid1 + 1
                r = mid2 - 1
            elif res == nums[mid1]:
                r = mid1 - 1
            else:
                l = mid2 + 1
        if r < l:
            nums = nums[:l] + [i] + nums[l:]
            continue
        if l == r:
            if l != 0:
                l -= 1
            else:
                r += 1
        print('{} {} {}'.format(i,nums[l],nums[r]), flush=True)
        res = int(input())
        if res == i:
            nums = nums[:r] + [i] + nums[r:]
        elif res == nums[l]:
            nums = nums[:l] + [i] + nums[l:]
        else:
            nums = nums[:r+1] + [i] + nums[r+1:]
    
    print(*nums, flush=True)
    input()

for i in range(t):
    solve(n)

exit()

# for i in range(1,51):
#     l = i//3
#     r = (i*2)//3
#     # print(i, l-1, r-l-1, i-r)
#     print(i,l,r)




