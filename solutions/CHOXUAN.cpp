#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("CHOXUAN.INP", "r", stdin);
    freopen("CHOXUAN.OUT", "w", stdout);

    long long n, k;
    cin >> n >> k;
    if (n >= 7 * k) cout << n - 7 * k;
    else cout << -1;
    return 0;
}
