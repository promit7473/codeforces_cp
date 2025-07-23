#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <cmath> // Include cmath for std::pow, though we will use our custom power function
 using namespace std;
 int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
     int n;
    cin >> n;
     while (n--){
        string word;
        cin >> word;
         if(word.length() > 10){
            cout << word[0]<<word.length()-2<<word.back() <<endl;
         } else{
            cout << word << endl;
        }
    }
    return 0;
}