#include <iostream>
#include <string>
 int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
     int n;
    std::cin >> n;
    int x = 0;
     for (int i = 0; i < n; ++i) {
        std::string statement;
        std::cin >> statement;
         if (statement[1] == '+') {
            x++;
        } else {
            x--;
        }
    }
     std::cout << x << std::endl;
     return 0;
}