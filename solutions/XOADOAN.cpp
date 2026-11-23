#include <bits/stdc++.h>
using namespace std;

int n;
long long s, p[100005];

int main() {
    freopen("XOADOAN.INP", "r", stdin);
    freopen("XOADOAN.OUT", "w", stdout);

    cin >> n;
    for (int i = 1; i <= n; i++) {
        long long x;
        cin >> x;
        p[i] = p[i - 1] + x;
    }
    cin >> s;

    if (p[n] <= s) {
        cout << 0;
        return 0;
    }

    // tim doan ngan nhat co tong >= need
    long long need = p[n] - s;
    int res = n + 1;
    deque<int> dq;
    for (int r = 0; r <= n; r++) {
        while (!dq.empty() && p[r] - p[dq.front()] >= need) {
            res = min(res, r - dq.front());
            dq.pop_front();
        }
        while (!dq.empty() && p[dq.back()] >= p[r]) dq.pop_back();
        dq.push_back(r);
    }

    if (res > n) res = -1;
    cout << res;
    return 0;
}
