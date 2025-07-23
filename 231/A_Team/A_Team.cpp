#include <iostream>
using namespace std;
 int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
     int n;
    cin >> n;
    int count = 0;
     while (n--) {
        int p, v, t;
        cin >> p >> v >> t;
         if (p + v + t >= 2) {
            count++;
        }
    }
     cout << count << endl;
     return 0;
}