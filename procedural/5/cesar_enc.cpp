#include <fstream>
#include <iostream>
#include <ostream>
#include <string>

using namespace std;

void _write(string filename, string data) {
  ofstream file;
  file.open(filename);

  if (file) {
    file << data << endl;
  }
  file.close();
  cout << "Your row has been written in file\n";
}

string _read(string filename) {
  string line;
  ifstream file(filename);
  if (file.is_open()) {
    getline(file, line);
  } else {
    cout << "File not found!";
  }
  file.close();
  return line;
}

void encrypt(string data, int n) {
  for (int i = 0; i < data.size(); i++) {
    char cur = data[i];
    data[i] = (char)(((int)cur) + n);
  }
  _write("encrypted.txt", data);
}

void decrypt(int n) {
  string data = _read("encrypted.txt");
  for (int i = 0; i < data.size(); i++) {
    char cur = data[i];
    data[i] = (char)(((int)cur) - n);
  }
  cout << data << "\n";
}

int main() {
  int n = 1;
  string raw;
  getline(cin, raw);
  cout << "Enter shift: ";
  cin >> n;
  encrypt(raw, n);
  decrypt(n);
}
