// Problem: A. Way Too Long Words
// Link: https://codeforces.com/problemset/problem/71/A

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    while (n--) {
        string word;
        cin >> word;
        if (word.length() > 10) {
            cout << word[0] << word.length() - 2 << word.back() << endl;
        } else {
            cout << word << endl;
        }
    }
    return 0;
}

