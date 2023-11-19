#include <algorithm>
#include <iostream>

using namespace std;

bool perestanovka(int *arr, int n) {
  for (int i = 0; i < n; ++i) {
    if (arr[i] == i) {
      return true;
    }
  }
  return false;
}

int main() {
  int ans = 0, n = 10, fac = 3628800;
  int arr[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  for (int i = 0; i < fac; ++i) {
    next_permutation(arr, arr + n);
    if (perestanovka(arr, n))
      ans++;
  }
  cout << ans << endl;

  return 0;
}