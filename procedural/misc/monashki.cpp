#include <iostream>
#include <map>
using namespace std;

void find_monashka(int target, int &n, int data[n][4], int keys[n],
                   map<int, int> table, int *res, int k) {
  int lowest[n];
  int j = 0;
  for (int i = 0; i < n; i++) {
    if (keys[i] < target) {
      lowest[j] = keys[i];
      j++;
    }
  }

  for (int i = 0; i < j; i++) {
    int key = table[lowest[i]];
    for (int m = 1; m < 4; m++) {
      if (data[key][m] == target) {
        res[k] = data[key][0];
        k++;
        if (target == 1) {
          return;
        }
        find_monashka(data[key][0], n, data, keys, table, res, k);
      }
    }
  }
  return;
}

int main() {

  int n, target, cur, first, second;
  cin >> n;

  int arr[n][4];
  int keys[n], res[n], f[n], s[n];
  map<int, int> table;
  cin >> target;
  cin >> first >> second;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < 4; j++) {
      cin >> cur;
      if (j == 0) {
        table[cur] = i;
        keys[i] = cur;
      }
      arr[i][j] = cur;
    }
  }
  find_monashka(target, n, arr, keys, table, res, 0);
  cout << "Ans for first task: ";
  for (int i = 0; i < n; i++) {
    cout << res[i] << " ";
    if (res[i] == 1) {
      break;
    }
  }
  cout << '\n';
  find_monashka(first, n, arr, keys, table, f, 0);
  find_monashka(second, n, arr, keys, table, s, 0);

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (f[i] == s[j]) {
        cout << "Ans for second task: " << f[i] << "\n";
        return 0;
      }
    }
  }
}