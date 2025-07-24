#include <iostream>
#include <vector>
 int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
     int t;
    std::cin >> t;
     while (t--) {
        int n;
        std::cin >> n;
         std::vector<int> round_numbers;
        int power_of_10 = 1;
         while (n > 0) {
            int digit = n % 10;
             if (digit != 0) {
                round_numbers.push_back(digit * power_of_10);
            }
             n /= 10;
            power_of_10 *= 10;
        }
         std::cout << round_numbers.size() << std::endl;
         for (size_t i = 0; i < round_numbers.size(); ++i) {
            std::cout << round_numbers[i] << (i == round_numbers.size() - 1 ? "" : " ");
        }
        std::cout << std::endl;
    }
     return 0;
}