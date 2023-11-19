#include <iostream>
using namespace std;

void hanoi(int n, int left, int mid, int right) {
  if (n == 1) {
    cout << left << " => " << right << " | ";
    return;
  }

  hanoi(n - 1, left, right, mid);
  cout << left << " => " << right << " | ";
  hanoi(n - 1, mid, left, right);
}

int main() {
  int n;

  cout << "Enter n: ";
  cin >> n;
  hanoi(n, 1, 2, 3);
  cout << "\n";
  return 0;
}
