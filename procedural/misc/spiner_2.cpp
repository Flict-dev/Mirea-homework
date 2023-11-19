#include <iostream>
using namespace std;
int main() {
  long n, l, m, ost, proc;
  cin >> n;

  ost = n / 7;
  l = ost, m = ost;
  proc = n % 7;
  switch (proc) {
  case 1:
    l--;
    m++;
    break;
  case 2:
    l += 2;
    m--;
    break;
  case 3:
    l++;
    break;
  case 4:
    m++;
    break;
  case 5:
    l += 3;
    m--;
  }
  cout << l << "\n" << m << "\n";
}
