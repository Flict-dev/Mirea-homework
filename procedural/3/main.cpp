#include <cctype>
#include <cmath>
#include <fstream>
#include <iostream>
#include <string>
#include <utility>
#include <algorithm>
using namespace std;

void zaem() {
  float m, s, p, n, r;
  cin >> s >> p >> n;
  r = p / 100;
  m = (s * r * pow((1 + r), n)) / (12 * (pow(1 + r, n) - 1));
  cout << m << endl;
}

void loan() {
  double s, m, n, r;
  cout << "S m n:" << endl;
  cin >> s >> m >> n;

  for (double p = 0.00001; p < 200; p+=0.00001) {
    r = p / 100;
    if (m <= (s * r * pow((1 + r), n) / (12 * (pow((1 + r), n) - 1)))){
      cout << p << endl;
      break;
    }
  } 
  // cout << "no\n";
}


void _write(string filename, string data) {
  ofstream file;
  file.open(filename);

  if (file) {
    file << data << endl;
  }
  file.close();
  cout << "Your row has been written in file\n"; 
}

string _read( string filename) {
  string line;
  ifstream file(filename);
  if (file.is_open()){
    getline(file, line);
  }else {
    cout << "File not found!";
  }
  file.close();
  return line;
}


void file_writer() {
  string filename, data;
  cout << "Enter filename: ";
  cin >> filename;
  cout << "Enter file data: ";
  cin >> data;
  _write(filename, data);
  string line = _read(filename);
  cout << line << endl;

}
  
void filter (){
  string filename;
  cout << "Enter filename: ";
  cin >> filename;
  string line = _read(filename);
  for (char sym: line){
    if (isdigit(sym)){
      cout << sym;
    }
  }
  cout << endl;

}

void bubbleSort(int arr[], int n)
{
    int i, j;
    bool swapped;
    for (i = 0; i < n - 1; i++) {
        swapped = false;
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
  
        // If no two elements were swapped
        // by inner loop, then break
        if (swapped == false)
            break;
    }
}


void printArray(int arr[], int size)
{
    int i;
    cout << "Your sorted row: " << "\n";
    for (i = 0; i < size; i++)
        cout << (char)arr[i];
    cout << "\n";
}

void row_sort(){
  
  string row;
  cout << "Enter row: ";
  getline(cin, row);

  int n = row.size();
  int chars[n];
  
  for (int i =0; i<n; i++ ){
    chars[i] = (int)row[i];
  }
  bubbleSort(chars, n);
  printArray(chars, n);
}


int main() { 
  
  // zaem(); 
  // file_writer();
  // filter();
  // loan();
  row_sort();
}