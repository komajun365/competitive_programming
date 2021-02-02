import numpy as np

n = int(input())
a_list = np.array(list(map(int, input().split())))
# a_list = np.array([3,4,2,1,5])

ans_list = a_list.argsort() + 1
print(' '.join(map(str, ans_list)))
