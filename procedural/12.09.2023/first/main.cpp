#include <iostream>
#include <string>
using namespace std;

// 1.1
void arifm() {
  float a, b;
  cout << "Enter A:";
  cin >> a;
  cout << "Enter B:";
  cin >> b;
  cout << "+ " << a + b << endl;
  cout << "- " << a - b << endl;
  cout << "* " << a * b << endl;
  if (b != 0) {
    cout << "/ " << a / b << endl;
  } else {
    cout << "Zero division error!" << endl;
  }
};
// 1.2
void equation() {
  float b, c;
  cout << "Enter B:";
  cin >> b;
  cout << "Enter C:";
  cin >> c;

  if (c == 0 && b == 0) {
    cout << "X is any\n";
  } else if (b != 0) {
    cout << -c / b << "\n";
  } else {
    cout << "No solution\n";
  }
}

// 1.3
void quad_equation() {
  double a;
  double b;
  double c;
  double x1, x2;
  cout << "Enter a: ";
  cin >> a;
  cout << "Enter b: ";
  cin >> b;
  cout << "Enter c: ";
  cin >> c;
  if (a != 0) {
    if ((b * b - 4 * a * c) >= 0) {
      x1 = (-1 * b + sqrt(b * b - 4 * a * c)) / (2 * a);
      x2 = (-1 * b - sqrt(b * b - 4 * a * c)) / (2 * a);
      if (x1 == x2) {
        cout << "Answer: " << x1 << endl;
      } else {
        cout << "First x: " << x1 << endl;
        cout << "Second x: " << x2 << endl;
      }
    } else {
      cout << "No solution!" << endl;
    }
  } else {
    if (c == 0 && b == 0) {
      cout << "X is any\n";
    } else if (b != 0) {
      cout << "Answer: " << -c / b << "\n";
    } else {
      cout << "No solution!" << endl;
    }
  }
}

// 1.4
void lamp() { 
  bool lamp, curtains, day;

  cout << "Enter lamp, curtains and day as 0 or 1: ";
  cin >> lamp >> curtains >> day;

  if ((day && curtains) || lamp) {
    cout << "Light" << endl;
  } else {
    cout << "Dark" << endl;
  }
}

int main() {
  // arifm();
  // equation();
  // quad_equation();
  // lamp();
}