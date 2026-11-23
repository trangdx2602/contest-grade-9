#include <bits/stdc++.h>
using namespace std;

int n;
long long k, a[200005], c[200005];

bool check(long long x) {
    // ban o p anh huong toi i khi (i-p)^2 < x
    long long w = sqrt((double)x);
    while (w * w >= x) w--;
    while ((w + 1) * (w + 1) < x) w++;

    __int128 s0 = 0, s1 = 0, s2 = 0;
    long long shots = 0;
    for (int i = 0; i < n; i++) {
        c[i] = 0;
        long long j = i - w - 1;
        if (j >= 0) {
            s0 -= c[j];
            s1 -= (__int128)c[j] * j;
            s2 -= (__int128)c[j] * j * j;
        }

        // sum c[p] * (x - (i-p)^2)
        __int128 dmg = x * s0 - ((__int128)i * i * s0 - 2 * i * s1 + s2);
        __int128 rem = a[i] - dmg;
        if (rem <= 0) continue;

        c[i] = (rem + x - 1) / x;
        shots += c[i];
        if (shots > k) return false;
        s0 += c[i];
        s1 += (__int128)c[i] * i;
        s2 += (__int128)c[i] * i * i;
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
