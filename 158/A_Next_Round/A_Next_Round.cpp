#include <iostream>
#include <vector>
 int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
     int n;
    int k;
    std::cin >> n >> k;
     std::vector<int> scores(n);
     for (int i = 0; i < n; ++i) {
        std::cin >> scores[i];
    }
     int kth_place_score = scores[k - 1];
     int advancers_count = 0;
     for (int i = 0; i < n; ++i) {
        if (scores[i] >= kth_place_score && scores[i] > 0) {
            advancers_count++;
        } else {
            break;
        }
    }
     std::cout << advancers_count << std::endl;
     return 0;
}