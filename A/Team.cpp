// Problem: A. Team
// Link: https://codeforces.com/problemset/problem/231/A

#include <iostream>
using namespace std;

int main() {
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

    cout << count << "\n";
    return 0;
}

