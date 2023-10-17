#include <array>
#include <cmath>
#include <deque>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <utility>
using namespace std;

void file_sum() {
  int n;
  cout << "Enter numms quatity: ";
  cin >> n;
  int nums[n];
  for (int i = 0; i < n; i++) {
    cin >> nums[i];
  }
  ofstream file;
  file.open("nums.txt");

  if (file) {
    for (int i = 0; i < n; i++) {
      file << nums[i] << endl;
    }
  }
  file.close();

  ifstream file_w("nums.txt");
  string num;
  int res;
  if (file_w.is_open()) {
    while (getline(file_w, num)) {
      res += stoi(num);
    }
  } else {
    cout << "File not found!";
  }
  file.close();

  cout << "Sum:" << res << "\n";
}

int sign(double num) {
  if (num > 0) {
    return 1;
  } else if (num < 0) {
    return -1;
  } else {
    return 0;
  }
}

double triangle_area(double a, double h) { return a * h * 0.5; }

double rectangle_area(double a, double b) { return a * b; }

double circle_area(double r) { return M_PI * r * r; }

void freedom_oil_iraq() {
  for (int i = 0; i < 6; i++) {
    for (int i = 0; i < 8; i++) {
      cout << "★";
    }
    for (int i = 0; i <= 15; i++) {
      cout << "-";
    }
    cout << "\n";
  }
  for (int i = 0; i < 7; i++) {
    for (int i = 0; i <= 23; i++) {
      cout << "-";
    }
    cout << "\n";
  }
}

void draw_sin() {
  int corner, newy, newx = 0;
  int step = 15;
  double y, x;
  char cord[1261][1261];

  for (int i = 0; i < 1261; i++) {
    for (int j = 0; j < 1261; j++) {
      cord[i][j] = '-';
    }
  }

  for (x = M_PI; x <= M_PI * 12; x += M_PI / 180) {
    corner = x * 180 / M_PI;
    if (corner / 180 == 0)
      y = 0;
    else
      y = sin(x);
    y = (int(y * 100) / 100.0) * step;
    y = round(y);

    newx = (int(x * 100) / 10.0 - 31);
    newy = int(y + step);

    cord[newx][newy] = '*';
  }

  for (int i = 0; i < step * 2 + 4; i++) {
    for (int j = 0; j < 346; j++) {
      cout << cord[j][i];
    }
    cout << endl;
  }
}

void to_roman() {
  map<string, int> all_roman = {
      {"M", 1000}, {"D", 500}, {"C", 100}, {"L", 50},
      {"X", 10},   {"V", 5},   {"I", 1},
  };
  int result = 0;

  string roman;
  cin >> roman;

  for (int i = 0; i < roman.size() - 1; ++i) {
    string current(1, roman[i]);
    string next_s(1, roman[i + 1]);
    if (all_roman[current] < all_roman[next_s])
      result += all_roman[next_s] - all_roman[current];
    else
      result += all_roman[current];
  }
  cout << result << "\n";
}

int randGen(int s, int m, int b, int c) {
  if (s == 0) {
    return 0;
  } else {
    return (m * randGen(s - 1, m, b, c) + b) % c;
  }
}

string alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

string _fromDecimal(int num, int s) {
  string res;

  while (num > 0) {
    res += alphabet[num % s];
    num /= s;
  }
  string rev;
  for (size_t i = res.size(); i > 0; --i) {
    rev += res[i - 1];
  }

  return rev;
}

int _toDecimal(string num, int s) {
  int res = 0;
  int j = 0;
  for (int i = num.size(); i > 0; --i) {
    if (alphabet.find(num[j]) > s - 1) {
      return 0;
    }
    res += pow(s, i - 1) * alphabet.find(num[j]);
    ++j;
  }
  return res;
}

void converter() {
  int n, oldn;
  string num;
  cout << "enter num, old notation, new notation\n";
  cin >> num >> oldn >> n;
  int newNum = _toDecimal(num, oldn);
  cout << _fromDecimal(newNum, n) << "\n";
}

int main() {
  // matrix();
  // converter();
  // draw_sin();
  // freedom_oil_iraq();
  // file_sum();
  // to_roman();  
  cout << randGen(2, 37, 3, 64) << "\n";
  cout << randGen(5, 25173, 13849, 65537) << "\n";
  cout << randGen(5, 5, 5, 5) << "\n";
}
