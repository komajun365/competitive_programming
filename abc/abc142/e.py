import numpy as np

n,m = map(int, input().split())

a_list = np.zeros(m+1).astype(int)
c_list = np.zeros(m+1).astype(int)

for i in range(1,m+1):
    a_list[i],b = map(int,input().split())
    c_s = list(map(int, input().split()))
    c_2 = 0
    for c in c_s:
        c_2 += 2**(c)
    c_list[i] = c_2

dp_list = np.full([n+1,m+1], 10**8).astype(int)
bit_list = np.zeros([n+1,m+1]).astype(int)
dp_list[0] = 0

for i in range(1,n+1):
    non_i_cost,non_i_bit = dp_list[i-1,0], bit_list[0,0]
    have_i_cost,have_i_bit = -1, bit_list[0,0]

    for j in range(1,m+1):
        before_cost,before_bit = dp_list[i-1,j] , bit_list[i-1,j]

        if(bin((before_bit >> i) & 1) == bin(1)):
            if(before_cost <= have_i_cost)|(have_i_cost == -1):
                have_i_cost,have_i_bit = before_cost,before_bit
        else:
            if(before_cost <= non_i_cost):
                non_i_cost,non_i_bit = before_cost ,before_bit

        c = c_list[j]
        if (bin((c >> i) & 1) == bin(1)) :
            if (non_i_cost + a_list[j] <= min(dp_list[i,j-1], (have_i_cost if have_i_cost != -1 else 10**9))):
                dp_list[i,j] = non_i_cost + a_list[j]
                bit_list[i,j] = non_i_bit | c_list[j]
            elif(dp_list[i,j-1] >= have_i_cost)&(have_i_cost != -1):
                dp_list[i,j], bit_list[i,j] = have_i_cost ,have_i_bit
            else:
                dp_list[i,j], bit_list[i,j] = dp_list[i,j-1], bit_list[i,j-1]


            # if ( dp_list[i,j-1] < non_i_cost + a_list[j]):
            #     dp_list[i,j], bit_list[i,j] = dp_list[i,j-1], bit_list[i,j-1]
            # else:
            #     dp_list[i,j] = non_i_cost + a_list[j]
            #     bit_list[i,j] = non_i_bit | c_list[j]
        else:
            if ( dp_list[i,j-1] < have_i_cost)|(have_i_cost == -1):
                dp_list[i,j], bit_list[i,j] = dp_list[i,j-1], bit_list[i,j-1]
            else:
                dp_list[i,j], bit_list[i,j] = have_i_cost ,have_i_bit


if(dp_list[n,m] >= 10**8):
    print(-1)
else:
    print(dp_list[n,m])

# print(dp_list)
