#include <iostream>

using namespace std;

void eratosphen() {
  int n, k;
  cin >> n;
  int data[n];
  for (int i = 0; i <= n; i++) {
    data[i] = i;
  }

  for (int i = 2; i <= n; i++) {
    if (data[i] != 0) {
      k = i * 2;
      for (int j = k; j <= n; j += i) {
        data[j] = 0;
      }
    }
  }
  for (int i = 2; i <= n; i++) {

    if (data[i] != 0) {
      cout << data[i] << " ";
    }
  }
  cout << "\n";
}

int main() { eratosphen(); }