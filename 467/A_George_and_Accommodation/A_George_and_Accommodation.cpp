#include<bits/stdc++.h>
using namespace std;
 using ll = long long int;
 inline void solve() {
  int n; cin >> n;
  int cnt = 0;
  while (n--) {
    int p, q; cin >> p >> q;
    if (q - p >= 2) cnt++;
  }
  cout << cnt << '\n';
}
int32_t main() {
  // #ifndef CHANDAK
  // freopen("input.txt","r",stdin); 
  // freopen("output.txt","w",stdout);
  // #endif
  ios_base::sync_with_stdio(0);
  cin.tie(NULL);
   int t; t = 1;
  while (t--) {
    solve();
  }
  return 0;
}