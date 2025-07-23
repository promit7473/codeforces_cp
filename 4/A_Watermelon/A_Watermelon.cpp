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
     if(n%2 == 0 && n >2){
        cout<<"YES";
    }
    else{
        cout<<"NO";
    }
    return 0;
}