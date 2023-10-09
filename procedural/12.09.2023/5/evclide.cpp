#include <iostream>

using namespace std;

void evclide() {
  int n, m;
  cin >> n >> m;
  while (n != m) {
    if (n > m) {
      n = n - m;
    } else {
      m = m - n;
    }
  }
  cout << n << "\n";
}
int main() { evclide(); }