#include <fstream>
#include <iostream>

const int SIZE = 21;

void readField(int field[SIZE][SIZE], std::ifstream &file) {
  for (int i = 0; i < SIZE; i++) {
    for (int j = 0; j < SIZE; j++) {
      char cell;
      file >> cell;
      field[i][j] = (cell == 'X') ? 1 : 0;
    }
  }
}

void writeField(int field[SIZE][SIZE], std::ofstream &file, bool b) {
  for (int i = 0; i < SIZE; i++) {
    for (int j = 0; j < SIZE; j++) {
      if (!b) {
        file << ((field[i][j] > 0) ? field[i][j] : 0);
      } else {
        file << ((field[i][j] != 0) ? field[i][j] : 1);
      }
    }
    file << std::endl;
  }
}

int countNeighbors(int field[SIZE][SIZE], int row, int col) {
  int count = 0;
  for (int i = -1; i <= 1; i++) {
    for (int j = -1; j <= 1; j++) {
      if (i == 0 && j == 0)
        continue;
      int neighborRow = row + i;
      int neighborCol = col + j;
      if (neighborRow >= 0 && neighborRow < SIZE && neighborCol >= 0 &&
          neighborCol < SIZE) {
        count += field[neighborRow][neighborCol];
      }
    }
  }
  return count;
}

void nextGenerationFn(int currentField[SIZE][SIZE], int nextField[SIZE][SIZE]) {
  for (int i = 0; i < SIZE; i++) {
    for (int j = 0; j < SIZE; j++) {
      int neighbors = countNeighbors(currentField, i, j);
      if (currentField[i][j] == 0) {
        nextField[i][j] = (neighbors == 3) ? 1 : 0;
      } else {
        nextField[i][j] =
            (neighbors == 2 || neighbors == 3) ? currentField[i][j] + 1 : 0;
      }
    }
  }
}

int countAlive(int field[SIZE][SIZE]) {
  int count = 0;
  for (int i = 0; i < SIZE; i++) {
    for (int j = 0; j < SIZE; j++) {
      count += field[i][j];
    }
  }
  return count;
}

int main() {
  std::ofstream outFile("work_out.txt");
  std::ifstream inFile("work_in.txt");

  int currentGeneration[SIZE][SIZE];
  int nextGeneration[SIZE][SIZE];

  readField(currentGeneration, inFile);

  int numGenerations;
  std::cout << "Введите количество поколений: ";
  std::cin >> numGenerations;

  for (int generation = 1; generation <= numGenerations; generation++) {
    outFile << "Поколение " << generation << ":" << std::endl;
    writeField(currentGeneration, outFile, false);

    nextGenerationFn(currentGeneration, nextGeneration);
    int aliveCount = countAlive(nextGeneration);

    if (aliveCount == 0) {
      std::cout << "Все микробы погибли." << std::endl;
      break;
    }

    std::cout << "Количество микробов в поколении " << generation << ": "
              << aliveCount << std::endl;
    outFile << "Поколение " << generation << "LOOOOOOOL:" << std::endl;
    writeField(currentGeneration, outFile, true);
    std::swap(currentGeneration, nextGeneration);
  }

  outFile.close();
  inFile.close();

  return 0;
}