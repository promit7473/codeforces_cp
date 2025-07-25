#include<bits/stdc++.h>
using namespace std;
 using ll = long long int;
 inline void solve() {
  int n; cin >> n;
  int a[n];
  for (int &i : a) cin >> i;
  sort(a, a + n);
  int ans = 1e9;
  for (int i = 1; i < n; ++i) {
    ans = min(ans, a[i] - a[i - 1]);
  }
  cout << ans << '\n';
}
int32_t main() {
  // #ifndef CHANDAK
  // freopen("input.txt","r",stdin); 
  // freopen("output.txt","w",stdout);
  // #endif
  ios_base::sync_with_stdio(0);
  cin.tie(NULL);
   int t; cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}