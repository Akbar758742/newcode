#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void max_beauty(int t) {
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        // Compute the global maximum and minimum of the array
        int global_max = *max_element(a.begin(), a.end());
        int global_min = *min_element(a.begin(), a.end());

        // Initialize the max beauty
        int max_beauty = 0;

        // Check beauty for all adjacent pairs
        for (int i = 0; i < n - 1; i++) {
            int max_outside = max(global_max, max(a[i], a[i + 1]));
            int min_outside = min(global_min, min(a[i], a[i + 1]));
            int max_inside = max(a[i], a[i + 1]);
            int min_inside = min(a[i], a[i + 1]);

            // Compute beauty for this pair
            int beauty = (max_outside - min_outside) + (max_inside - min_inside);
            max_beauty = max(max_beauty, beauty);
        }

        // Output the result for this test case
        cout << max_beauty << endl;
    }
}

int main() {
    int t;
    cin >> t;
    max_beauty(t);
    return 0;
}

