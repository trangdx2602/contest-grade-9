#include <bits/stdc++.h>
using namespace std;

int n;
long long k, a[100005], b[100005];

bool exist(long long x) {
    return binary_search(b, b + n, x);
}

int main() {
    freopen("CANBANG.INP", "r", stdin);
    freopen("CANBANG.OUT", "w", stdout);

    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        b[i] = a[i];
    }
    sort(b, b + n);

    int res = 0;
    for (int i = 0; i < n; i++)
        if (exist(a[i] - k) && exist(a[i] + k)) res++;
    cout << res;
    return 0;
}
