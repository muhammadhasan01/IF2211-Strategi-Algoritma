#include <bits/stdc++.h>

using namespace std;

clock_t timer;

int main() { 
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, W;
    cin >> n >> W;
    vector<long long> v(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> v[i];
    }
    vector<long long> w(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> w[i];
    }
    cout << "Time Limit (T) = " << W << '\n';
    cout << "There are " << n << " activities with a format of a = (p, t):\n";
    for (int i = 1; i <= n; i++) {
        cout << "(" << v[i] << "," << w[i] << ")" << (i == n ? "\n\n" : ",");
    }
    timer = clock();
    vector<vector<long long>> dp(n + 1, vector<long long>(W + 1));
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= W; j++) {
            if (i == 0 || j == 0) {
                dp[i][j] = 0LL;
            } else {
                dp[i][j] = dp[i - 1][j];
                if (w[i] <= j) {
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - w[i]] + v[i]);
                }
            }
            
        }
    }
    long long max_val = dp[n][W];
    vector<int> answer;
    int i = n, j = W;
    while (i > 0) {
        if (dp[i][j] == dp[i - 1][j]) {
            i--;
        } else {
            answer.push_back(i);
            j -= w[i];
            i--;
        }
    }
    reverse(answer.begin(), answer.end());
    double timeNeeded = (1000.0) * (clock() - timer) / CLOCKS_PER_SEC;
    cout << "Maximal total priority value = " << max_val << '\n';
    cout << "The optimal chosen sequence of activity is ";
    cout << answer.size() << " activities:\n";
    for (auto& e : answer) {
        cout << e << " ";
    }
    cout << '\n';
    cout << "Execution Time : ";
    cout << fixed << setprecision(5) << timeNeeded << "ms\n";

    return 0;
}