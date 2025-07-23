#include <bits/stdc++.h>
using namespace std;
 using ll = long long int;
 int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
        int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        vector<int> a(n);
        for (int i = 0; i < n; ++i)
            cin >> a[i];
                int hikes = 0;
        int i = 0;
                while (i <= n - k) {
                        bool can_hike = true;
            for (int j = 0; j < k; ++j) {
                if (a[i + j] != 0) {
                    can_hike = false;
                    break;
                }
            }
            if (can_hike) {
                ++hikes;
                i += k + 1; 
            } else {
                ++i;
            }
        }
                cout << hikes << "\n";
    }
     return 0;
}