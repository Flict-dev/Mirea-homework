import zipfile
import time
import csv
import shutil
import tempfile
import tkinter as tk
from tkinter import scrolledtext
from commands import CommandDispatcher


class ShellEmulator:
    def __init__(self, config_path):
        self.load_config(config_path)
        self.temp_dir = tempfile.mkdtemp()  # Временная директория для распаковки
        self.load_filesystem()
        self.current_path = self.temp_dir  # Текущая директория
        self.log_file = open(self.log_path, 'w', newline='')
        self.logger = csv.writer(self.log_file)
        self.logger.writerow(['Timestamp', 'Command'])
        self.dispatcher = CommandDispatcher()

    def load_config(self, config_path):
        """Чтение конфигурации из CSV"""
        with open(config_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                key, value = row
                if key == "hostname":
                    self.hostname = value
                elif key == "filesystem_path":
                    self.fs_path = value
                elif key == "log_path":
                    self.log_path = value
                elif key == "startup_script":
                    self.startup_script = value

    def load_filesystem(self):
        """Распаковка файловой системы из zip-архива во временную директорию"""
        with zipfile.ZipFile(self.fs_path, 'r') as zip_ref:
            zip_ref.extractall(self.temp_dir)

    def execute_command(self, command):
        """Выполнение команды"""
        result = self.dispatcher.execute(command)
        self.log_command(command)
        return result

    def log_command(self, command):
        """Логирование команды"""
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.logger.writerow([timestamp, command])

    def start_gui(self):
        """Запуск GUI интерфейса для ввода команд"""
        root = tk.Tk()
        root.title("Shell Emulator")
        text_area = scrolledtext.ScrolledText(root, width=80, height=20)
        text_area.grid(column=0, row=0)
        input_field = tk.Entry(root, width=80)
        input_field.grid(column=0, row=1)

        def process_input(event):
            command = input_field.get()
            text_area.insert(tk.END, f"{self.hostname}> {command}\n")
            cmd_res = self.execute_command(command)
            if cmd_res == "clear":
                text_area.delete('1.0', tk.END)
            else:
                text_area.insert(tk.END, f"{cmd_res}\n")
            input_field.delete(0, tk.END)
            
        input_field.bind("<Return>", process_input)
        root.mainloop()

    def exit_shell(self):
        """Команда exit: завершение сеанса"""
        self.log_file.close()
        shutil.rmtree(self.temp_dir)  # Удаляем временную директорию
        exit(0)


# Запуск эмулятора
if __name__ == "__main__":
    config_file = "config.csv"
    emulator = ShellEmulator(config_file)
    emulator.start_gui()