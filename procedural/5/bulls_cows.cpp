#include <algorithm>
#include <iostream>
#include <random>
#include <string>

using namespace std;

int main() {
  random_device dev;
  mt19937 rng(dev());
  uniform_int_distribution<mt19937::result_type> dist(1000, 9999);
  string guess = to_string(dist(rng));
  string cur;
  cout << guess << "\n";
  while (true) {
    cout << "Enter your guess: ";
    cin >> cur;
    string res = "";
    if (stoi(cur) > 9999) {
      cout << "WTF?! are u dumb?!"  << "\n";
      continue;
    }
    cout << "****" << "\n";
    for (int i = 0; i < guess.size(); i++) {
      char g_sym = guess[i];
      char c_sym = cur[i];
      if (g_sym == c_sym) {
        res += "+";
      } else if (guess.find(c_sym) != -1) {
        res += "-";
      } else {
        res += " ";
      }
    }
    cout << res << "\n";
    if (res == "++++"){
        break;
    }
  }
  cout << "GG" << "\n";
}
