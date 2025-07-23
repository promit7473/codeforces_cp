#include <iostream>
 int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
     int M, N;
    std::cin >> M >> N;
     int total_area = M * N;
     int max_dominoes = total_area / 2;
     std::cout << max_dominoes << std::endl;
     return 0;
}