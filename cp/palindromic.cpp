#include<bits/stdc++.h>
using namespace std;
bool isPalindrome(const string& s, int left, int right) {
    while (left < right) {
        if (s[left] != s[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

int main() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    if (isPalindrome(s, 0, n - 1)) {
        cout << n << endl;
        return 0;
    }
    int left = 0, right = n - 1;

    while (left < right && s[left] == s[right]) {
        left++;
        right--;
    }

    int maxLength = 0;
    if (isPalindrome(s, left + 1, right)) {
        maxLength = max(maxLength, right - left);
    }
    if (isPalindrome(s, left, right - 1)) {
        maxLength = max(maxLength, right - left);
    }
    cout << n - (right - left + 1) + maxLength << endl;
    return 0;
}