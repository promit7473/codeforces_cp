#include <iostream>
#include <vector>
#include <algorithm>
 struct Element {
    int value;
    int original_index;
};
 bool compareElements(const Element& a, const Element& b) {
    return a.value < b.value;
}
 int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    int t;
    std::cin >> t;
    while (t--) {
        int n;
        std::cin >> n;
        std::vector<Element> elements(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> elements[i].value;
            elements[i].original_index = i + 1;
        }
         std::sort(elements.begin(), elements.end(), compareElements);
         if (elements[0].value != elements[1].value) {
            std::cout << elements[0].original_index << std::endl;
        } else {
            std::cout << elements[n-1].original_index << std::endl;
        }
    }
    return 0;
}