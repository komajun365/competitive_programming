'''
長さ N の配列に対し、
・要素の 1 点変更(加算)
・区間の要素の総和
を O(logN) で求めることが出来るデータ構造です。

要素はintとしておきます。
※modを設定し、modintっぽく振る舞うようにしておきます。

初期値は0。

'''


class FenwickTree:
    def __init__(self, n: int):
        self.__n = n
        self.__data = [0] * self.__n

    def add(self, p: int, x: int):
        assert (0 <= p) & (p < self.__n)
        p += 1
        while(p <= self.__n):
            self.__data[p - 1] += x
            p += p & -p

    def sum(self, l: int, r: int):
        assert (0 <= l) & (l <= r) & (r <= self.__n)
        return self.__sum(r) - self.__sum(l)


    def __sum(self, r: int):
        s = 0
        while(r > 0):
            s += self.__data[r - 1]
            r -= r & -r
        return s

