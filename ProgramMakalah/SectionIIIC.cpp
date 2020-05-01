#include <bits/stdc++.h>

using namespace std;

const int N = 1e5 + 5;

struct activity {
  int p, s, e;
  int idx;
  bool operator<(const activity& other) {
    if (s == other.s)
      return e < other.e;
    return s < other.s;
  }
};

int n;
activity a[N];
int dp[N];
int go[N];
clock_t timer;

int main() { 
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> a[i].p >> a[i].s >> a[i].e;
    a[i].idx = i;
  }
  cout << "There are " << n << " activities with a format a = (p, s, e):\n";
  for (int i = 1; i <= n; i++) {
      cout << "(" << a[i].p << "," << a[i].s << "," << a[i].e << ")";
      cout << (i == n ? "\n\n" : ",");
  }
  timer = clock();
  sort(a + 1, a + 1 + n);
  for (int i = 1; i <= n; i++) {
    dp[i] = a[i].p;
    for (int j = 0; j < i; j++) {
      if (j == 0 || a[j].e < a[i].s) {
        int cur = dp[j] + a[i].p;
        if (cur > dp[i]) {
          dp[i] = cur;
          go[i] = j;
        }
      }
    }
  }
  int ans = 0;
  int pos = 0;
  for (int i = 1; i <= n; i++) {
    if (dp[i] > ans) {
      ans = dp[i];
      pos = i;
    }
  }
  int i = pos;
  vector<int> answer;
  while (i > 0) {
    answer.push_back(a[i].idx);
    i = go[i];
  }
  double timeNeeded = (1000.0) * (clock() - timer) / CLOCKS_PER_SEC;
  cout << "Maximum total priority value = " << ans << '\n';
  cout << "The optimal chosen sequence of activity is ";
  cout << answer.size() << " activities:\n";
  for (auto e : answer) cout << e << ' ';
  cout << '\n';
  cout << fixed << setprecision(5) << "Execution Time: " << timeNeeded << "ms\n";

  return 0;
}