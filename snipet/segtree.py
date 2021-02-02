# segment木を実装する

class Seg_min():
    def __init__(self,x):
        #####単位元######
        self.ide_ele_min = 10**10
        self.func = min

        self.n = len(x)

        #num_max:n以上の最小の2のべき乗
        self.num_max =2**(self.n-1).bit_length()
        self.x = [self.ide_ele_min]*2*self.num_max

        for i,num in enumerate(x, self.num_max):
            self.x[i] = num
        for i in range(self.num_max-1,0,-1):
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def update(self,i,x):
        i += self.num_max
        self.x[i] = x
        while(i>0):
            i = i//2
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def query(self,i,j):
        res = self.ide_ele_min
        if i>=j:
            return res
        i += self.num_max
        j += self.num_max -1
        while(i<=j):
            if(i==j):
                res = self.func(res,self.x[i])
                break
            if(i&1):
                res = self.func(res,self.x[i])
                i += 1
            if(not j&1):
                res = self.func(res,self.x[j])
                j -= 1
            i = i>>1
            j = j>>1
        return res


class Seg_max():
    def __init__(self,x):
        #####単位元######
        self.ide_ele_min = 10**10 * -1
        self.func = max

        self.n = len(x)

        #num_max:n以上の最小の2のべき乗
        self.num_max =2**(self.n-1).bit_length()
        self.x = [self.ide_ele_min]*2*self.num_max

        for i,num in enumerate(x, self.num_max):
            self.x[i] = num
        for i in range(self.num_max-1,0,-1):
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def update(self,i,x):
        i += self.num_max
        self.x[i] = x
        while(i>0):
            i = i//2
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def query(self,i,j):
        res = self.ide_ele_min
        if i>=j:
            return res
        i += self.num_max
        j += self.num_max -1
        while(i<=j):
            if(i==j):
                res = self.func(res,self.x[i])
                break
            if(i&1):
                res = self.func(res,self.x[i])
                i += 1
            if(not j&1):
                res = self.func(res,self.x[j])
                j -= 1
            i = i>>1
            j = j>>1
        return res











#　元ネタ
# https://juppy.hatenablog.com/entry/2019/11/13/%E6%9C%80%E5%A4%A7%E3%83%BB%E6%9C%80%E5%B0%8F%E3%82%BB%E3%82%B0%E6%9C%A8_%E3%82%B3%E3%83%94%E3%83%9A%E7%94%A8_Python

# # 最小値を求めるセグメント木
# def init_min(init_min_val):
#     #set_val
#     for i in range(n):
#         seg_min[i+num_max-1]=init_min_val[i]
#     #built
#     for i in range(num_max-2,-1,-1) :
#         seg_min[i]=min(seg_min[2*i+1],seg_min[2*i+2])
#
# def update_min(k,x):
#     k += num_max-1
#     seg_min[k] = x
#     while k:
#         k = (k-1)//2
#         seg_min[k] = min(seg_min[k*2+1],seg_min[k*2+2])
#
# # p以上q未満の最小値を返す
# def query_min(p,q):
#     if q<=p:
#         return ide_ele_min
#     p += num_max-1
#     q += num_max-2
#     res=ide_ele_min
#     while q-p>1:
#         if p&1 == 0:
#             res = min(res,seg_min[p])
#         if q&1 == 1:
#             res = min(res,seg_min[q])
#             q -= 1
#         p = p//2
#         q = (q-1)//2
#     if p == q:
#         res = min(res,seg_min[p])
#     else:
#         res = min(min(res,seg_min[p]),seg_min[q])
#     return res
#
# #####単位元######
# ide_ele_min = 10**10
#
# #num_max:n以上の最小の2のべき乗
# # num_max =2**(n-1).bit_length()
# num_max = 2**(len(str(bin(n-1))) -2)
# seg_min=[ide_ele_min]*2*num_max
#
#
#
# #########################################
#
# # 最大値を求めるセグメント木
#
# def init_max(init_max_val):
#     #set_val
#     for i in range(n):
#         seg_max[i+num_max-1]=init_max_val[i]
#     #built
#     for i in range(num_max-2,-1,-1) :
#         seg_max[i]=max(seg_max[2*i+1],seg_max[2*i+2])
#
# def update_max(k,x):
#     k += num_max-1
#     seg_max[k] = x
#     while k:
#         k = (k-1)//2
#         seg_max[k] = max(seg_max[k*2+1],seg_max[k*2+2])
#
# def query_max(p,q):
#     if q<=p:
#         return ide_ele_max
#     p += num_max-1
#     q += num_max-2
#     res=ide_ele_max
#     while q-p>1:
#         if p&1 == 0:
#             res = max(res,seg_max[p])
#         if q&1 == 1:
#             res = max(res,seg_max[q])
#             q -= 1
#         p = p//2
#         q = (q-1)//2
#     if p == q:
#         res = max(res,seg_max[p])
#     else:
#         res = max(max(res,seg_max[p]),seg_max[q])
#     return res
#
# #####単位元######
# ide_ele_max = -1
#
# #num_max:n以上の最小の2のべき乗
# # num_max =2**(n-1).bit_length()
# num_max = 2**(len(str(bin(n-1))) -2)
# seg_max=[ide_ele_max]*2*num_max
