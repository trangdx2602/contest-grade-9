#include <bits/stdc++.h>
using namespace std;

int n, q, cnt[26][100005];
string s;

int dist(int x, int y) {
    int d = abs(x - y);
    return min(d, 26 - d);
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    freopen("KHOANGCACH.INP", "r", stdin);
    freopen("KHOANGCACH.OUT", "w", stdout);

    cin >> s >> q;
    n = s.size();
    for (int c = 0; c < 26; c++)
        for (int i = 1; i <= n; i++)
            cnt[c][i] = cnt[c][i - 1] + (s[i - 1] - 'a' == c);

    while (q--) {
        int l, r;
        cin >> l >> r;
        vector<int> v;
        for (int c = 0; c < 26; c++)
            if (cnt[c][r] > cnt[c][l - 1]) v.push_back(c);

        int res = 0;
        for (int i = 0; i < (int)v.size(); i++)
            for (int j = i + 1; j < (int)v.size(); j++)
                res = max(res, dist(v[i], v[j]));
        cout << res << '\n';
    }
    return 0;
}
