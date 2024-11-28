#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

// Define a hash function for unordered_map to store states
struct HashFunction {
    size_t operator()(const vector<int>& v) const {
        size_t hash = 0;
        for (int x : v) {
            hash = hash * 31 + x;
        }
        return hash;
    }
};

// Recursive function with memoization
int countWays(vector<vector<int>>& matrix, int row, vector<int>& columnSums, unordered_map<vector<int>, int, HashFunction>& memo) {
    if (row == matrix.size()) {
        return (columnSums[0] == columnSums[1] && columnSums[1] == columnSums[2]) ? 1 : 0;
    }

    if (memo.count(columnSums)) return memo[columnSums];

    int ways = 0;

    // Try converting each element in the current row to 0
    for (int col = 0; col < 3; ++col) {
        int originalValue = matrix[row][col];
        columnSums[col] -= originalValue;  // Remove this value from the column sum

        ways += countWays(matrix, row + 1, columnSums, memo);

        columnSums[col] += originalValue;  // Backtrack to restore the column sum
    }

    return memo[columnSums] = ways;
}

int main() {
    int n;
    cin >> n;

    vector<vector<int>> matrix(n, vector<int>(3));
    vector<int> columnSums(3, 0);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < 3; ++j) {
            cin >> matrix[i][j];
            columnSums[j] += matrix[i][j];
        }
    }

    unordered_map<vector<int>, int, HashFunction> memo;
    cout << countWays(matrix, 0, columnSums, memo) << endl;

    return 0;
}
