#include <fstream>
#include <iostream>
#include <map>
#include <stack>
#include <string>
#include <vector>

using namespace std;

vector<string> _read(string filename) {
  vector<string> data;

  string line;
  ifstream file(filename);
  if (file.is_open()) {
    while (getline(file, line)) {
      data.push_back(line);
    };
  } else {
    cout << "File not found!";
  }
  file.close();
  return data;
}

int main() {
  map<char, int> o_brackets = {
      {'(', 1},
      {'{', 2},
      {'[', 3},
  };
  map<char, int> c_brackets = {
      {')', 1},
      {'}', 2},
      {']', 3},
  };

  stack<int> stack;

  vector<string> data = _read("test.txt");

  for (int i = 0; i < data.size(); i++) {
    string cur = data[i];
    for (char el : cur) {
      if (o_brackets.count(el)) {
        stack.push(o_brackets[el]);
      } else {
        int o_el = stack.top();
        if (o_el == c_brackets[el]) {
          stack.pop();
        } else {
          break;
        }
      }
    }
    cout << "Row: " << cur << " ";
    if (!stack.size()) {
      cout << "TRUE"
           << "\n";
    } else {
      cout << "FALSE"
           << "\n";
    }
  }
}