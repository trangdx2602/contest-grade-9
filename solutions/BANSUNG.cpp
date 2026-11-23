#include <bits/stdc++.h>
using namespace std;

int n;
long long k, a[200005], c[200005];

bool check(long long x) {
    // ban cach bia i mot khoang d gay x - d^2, chi co tac dung khi d <= w
    long long w = sqrt((double)x);
    while (w * w >= x) w--;
    while ((w + 1) * (w + 1) < x) w++;

    long long s0 = 0, t1 = 0, t2 = 0;   // tong c, c*d, c*d^2 cua cac phat con tac dung
    long long shots = 0;
    for (int i = 0; i < n; i++) {
        c[i] = 0;
        if (i > 0) {
            // sang bia moi, moi khoang cach d tang len 1
            t2 += 2 * t1 + s0;
            t1 += s0;
            long long j = i - w - 1;
            if (j >= 0) {
                s0 -= c[j];
                t1 -= c[j] * (w + 1);
                t2 -= c[j] * (w + 1) * (w + 1);
            }
        }

        long long rem = a[i] - (x * s0 - t2);
        if (rem <= 0) continue;

        c[i] = (rem + x - 1) / x;
        shots += c[i];
        if (shots > k) return false;
        s0 += c[i];
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    freopen("BANSUNG.INP", "r", stdin);
    freopen("BANSUNG.OUT", "w", stdout);

    cin >> n >> k;
    long long mx = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        mx = max(mx, a[i]);
    }

    long long l = 1, r = mx + 1LL * (n - 1) * (n - 1);
    while (l < r) {
        long long mid = (l + r) / 2;
        if (check(mid)) r = mid;
        else l = mid + 1;
    }
    cout << l;
    return 0;
}
