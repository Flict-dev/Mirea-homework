## Запуск скрипта

В program.txt записываются команды (LOAD, READ, WRITE, SHIFT)
1. LOAD загрузка константы в регистр
2. READ чтение из памяти в регистр
3. WRITE запись з памяти в регистр
4. SHIFT побитовый сдвиг влево регистра на занчение из памяти

Запуск ассемблера
```bash
python assembler.py program.txt program.bin program_log.csv
```
Запуск интерпретатора
```bash
python interpreter.py program.bin result.csv 20 32
```


## Тестирование
```bash
pip install pytest
pytest -v tests.py
```