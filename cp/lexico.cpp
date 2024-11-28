#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Function to find the lexicographically maximum position for replacement
int findMaxPos(const string& s, char ch) {
    int n = s.size();
    int maxPos = -1;

    for (int i = 0; i < n; ++i) {
        if (s[i] < ch) {
            if (maxPos == -1 || s[maxPos] < s[i]) {
                maxPos = i;
            }
        }
    }
    return maxPos + 1; // Convert to 1-based index
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n, q;
        cin >> n >> q;

        string s;
        cin >> s;

        while (q--) {
            char ch;
            cin >> ch;

            int pos = findMaxPos(s, ch);
            cout << pos << '\n';

            // Apply the change permanently
            if (pos > 0) {
                s[pos - 1] = ch; // Change to 0-based index
            }
        }
    }

    return 0;
}

