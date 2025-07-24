#include <iostream>
 int main() {
    // Optimize C++ standard streams for faster input/output.
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
     int t;
    std::cin >> t; // Read the number of test cases
     while (t--) { // Loop through each test case
        int a, b;
        std::cin >> a >> b; // Correctly read both a and b
         if (a % b == 0) {
            // If 'a' is already divisible by 'b', 0 moves are needed.
            std::cout << 0 << std::endl;
        } else {
            // If 'a' is not divisible by 'b':
            // Calculate the remainder when 'a' is divided by 'b'.
            int remainder = a % b;
            // The number of moves needed is 'b' minus the remainder.
            std::cout << b - remainder << std::endl;
        }
    }
     return 0;
}