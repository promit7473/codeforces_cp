#include <iostream>
#include <cmath>
 int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
     int value;
    int row_one = -1;
    int col_one = -1;
     for (int i = 1; i <= 5; ++i) {
        for (int j = 1; j <= 5; ++j) {
            std::cin >> value;
            if (value == 1) {
                row_one = i;
                col_one = j;
            }
        }
    }
     int moves_row = std::abs(row_one - 3);
    int moves_col = std::abs(col_one - 3);
     int total_moves = moves_row + moves_col;
     std::cout << total_moves << std::endl;
     return 0;
}