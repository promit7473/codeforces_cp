#include<bits/stdc++.h>
using namespace std;
 using ll = long long int;
 int32_t main() {
    // Optional: for faster input/output
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
        int t; 
    cin >> t;
    while (t--) {
        int x;
        cin >> x;
        string s = to_string(x);
        char smallest_digit = *min_element(s.begin(), s.end());
                cout << smallest_digit << "\n";
    }
        return 0;
}