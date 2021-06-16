#include <cmath>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

long long square(const int &x) { return 1LL * x * x; }

int main() {
    int n, m;

    cin >> n >> m;
    vector<int> l(n);
    for (int i = 0; i < n; ++i) {
        cin >> l[i];
    }

    unordered_map<long long, int> map;
    long long ans = 0;
    if (n > 1) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                long long sum = square(l[i]) + square(l[j]);
                long long diff = abs(square(l[i]) - square(l[j]));
                map[sum * 2]++;
                map[diff * 2]++;
            }

            long long s = square(l[i]);
            if (map.count(s * 2) > 0) {
                ans += map[s * 2];
            }
        }
    }

    unordered_map<long long, int> map2;
    // mから二本使う場合の追加
    if (m > 1) {
        for (int i = 0; i < n; ++i) {
            long long s = square(l[i]);
            map2[s]++;
        }
    }

    long long maxv = 0;
    // mを最大数使えるパターンを探す
    for (auto &p : map) {
        int v = p.second;
        long long key = p.first;
        if (key == 0)
            continue;
        int v2 = map2.count(key) ? map2[key] : 0;
        long long sum = (long long)v * m + m * (m - 1) * v2 / 2;

        maxv = max(maxv, sum);
    }
    for (auto &p : map2) {
        int v = p.second;
        long long sum = (long long)m * (m - 1) * v / 2;

        maxv = max(maxv, sum);
    }

    cout << ans + maxv << endl;

    return 0;
}