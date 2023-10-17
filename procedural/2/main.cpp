#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>

using namespace std;

// 2.1
void conus() {
  // 6 3 5
  float h, r, R;
  cin >> h >> r >> R;
  float v = 1.0 / 3 * M_PI * h * (R * R + R * r + r * r);
  float l = sqrt(h * h + (R - r) * (R - r));
  float s = M_PI * (R * R + l * (R + r) + r * r);
  cout << v << endl;
  cout << s << endl;
  cout << l << endl;
}
// 2.2
void split() {
  float x, a, w, l;
  cin >> x >> a;
  if (abs(x) < 1) {
    if (x != 0) {
      if (a == 0){
        w = 0;
      } else {
        w = a * log(abs(x));
      }
}
  } else {
    l = a - x * x;
    if (l >= 0) {
      w = sqrt(l);
    } else {
      w = 0;
    }
  }
  
  cout << abs(w) << endl;
}

// 2.3
void func() {
  float x, y, b, z;
  cin >> x >> y >> b;
  if ((b - y) > 0 && (b - x) >= 0) {
    z = log((b - y)) * sqrt(b - x);
  } else {
    cout << "Lox" << endl;
  }
}

void sequence() {
  int n;
  cin >> n;
  for (int i = 0; i <= 10; ++i){
    cout << n + i << " ";
  }
  cout << endl; 
}

void tabulation() {
  double x, y;

  for (x = -4.0; x <=4; x+=0.5){
    if (x-1 != 0){
      y = (x*x - 2*x + 2) / (x - 1);
      cout << y << endl;
    }
  }
}

int main() {
  // conus();
  // split();
  // func();
  // sequence();
  // tabulation();

}