#include <cmath>
#include <fstream>
#include <iostream>
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
  int corner, newy, newx, size = 0;
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
    size++;
    cout << newy << " " << newx << endl;
    cord[newx][newy] = '*';
  }

  for (int i = 0; i < step * 2 + 4; i++) {
    for (int j = 0; j < 346; j++) {
      cout << cord[j][i];
    }
    cout << endl;
  }
}


int main() { draw_sin(); }