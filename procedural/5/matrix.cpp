#include <fstream>
#include <iostream>
#include <iterator>
#include <string>
using namespace std;

void **_write_matrix(double **data, int n, int m, string info) {
  ofstream file;
  file.open("matrix.txt", ios::app);

  if (file) {
    file << info << "\n";
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        file << data[i][j] << "\t";
      }
      file << "\n";
    }
    file << "\n";
  }
  file.close();
  cout << "Your matrix has been written in file: " << info <<"\n";
  return 0;
}

double **gen_matrix(unsigned int n, unsigned int m) {
  double **data = new double *[n];
  for (int i = 0; i < n; i++) {
    data[i] = new double[m];
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      data[i][j] = i + j;
    }
  }
  return data;
}

double **gen_e_matrix(unsigned int n, unsigned int m) {
  double **data = new double *[n];
  for (int i = 0; i < n; i++) {
    data[i] = new double[m];
  }
  int idx = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (j == idx) {
        data[i][j] = 1;
      } else {
        data[i][j] = 0;
      }
    }
    idx ++;
  }
  return data;
}

double **gen_c_matrix(unsigned int n, unsigned int m) {
  double **data = new double *[n];
  for (int i = 0; i < n; i++) {
    data[i] = new double[m];
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (i + j != 0) {
        data[i][j] = 1.0 / (i + j);
      } else {
        data[i][j] = 0;
      }
    }
  }
  return data;
}

double **calculate(double **data1, double **data2, char operand, int n) {
  double **new_matrix;
  new_matrix = gen_matrix(n, n);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      switch (operand) {
      case '+':
        new_matrix[i][j] = data1[i][j] + data2[i][j];
        break;
      case '-':
        new_matrix[i][j] = data1[i][j] - data2[i][j];
        break;
      case '*':
        new_matrix[i][j] = data1[i][j] * data2[i][j];
        break;
      }
    }
  }
  return new_matrix;
}
int main() {
  int n;
  cin >> n;
  double **a_matrix;
  double **b_matrix;
  double **c_matrix;
  double **e_matrix;
  double **b_e_matrix;
  double **a_b_e_matrix;
  double **a_b_e_c_matrix;

  // создание массива
  a_matrix = gen_matrix(n, n);
  b_matrix = gen_matrix(n, n);
  c_matrix = gen_c_matrix(n, n);
  e_matrix = gen_e_matrix(n, n);
  _write_matrix(a_matrix, n, n, "A a_matrix");
  _write_matrix(b_matrix, n, n, "B b_matrix");
  _write_matrix(c_matrix, n, n, "C c_matrix");
  _write_matrix(e_matrix, n, n, "E e_matrix");
  b_e_matrix = calculate(b_matrix, e_matrix, '-', n);
  _write_matrix(b_e_matrix, n, n, "B-E matrix");
  a_b_e_matrix = calculate(a_matrix, b_e_matrix, '*', n);
  _write_matrix(a_b_e_matrix, n, n, "A(B-E) matrix");
  a_b_e_c_matrix = calculate(a_b_e_matrix, c_matrix, '+', n);
  _write_matrix(a_b_e_c_matrix, n, n, "M=A(B-E)+C matrix");
}