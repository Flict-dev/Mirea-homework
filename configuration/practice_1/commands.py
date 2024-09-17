import os
from abc import ABC, abstractmethod


class BaseCommand(ABC):
    @staticmethod
    @abstractmethod
    def run(*args) -> str:
        """Метод для выполнения команды"""
        pass

    @staticmethod
    @abstractmethod
    def parse_args(args):
        """Парсинг аргументов для команды"""
        pass

    @staticmethod
    def error(message: str) -> str:
        """Возвращает сообщение об ошибке"""
        return f"Error: {message}"


# Команда ls
class LSCommand(BaseCommand):
    @staticmethod
    def run(command: str, current_path: str, *args) -> str:
        parsed_args = LSCommand.parse_args(args)
        target_dir = os.path.join(current_path, parsed_args)
        try:
            files = os.listdir(target_dir)
            return '\n'.join(files)
        except FileNotFoundError:
            return LSCommand.error(f"ls: cannot access '{target_dir}': No such file or directory")

    @staticmethod
    def parse_args(args):
        return args[0] if args else '.'


class CDCommand(BaseCommand):
    @staticmethod
    def run(command: str, current_path: str, *args) -> str:
        target_path = CDCommand.parse_args(args)
        new_path = os.path.join(current_path, target_path)
        if os.path.isdir(new_path):
            return os.path.abspath(new_path)
        else:
            return CDCommand.error(f"cd: no such file or directory: {target_path}")

    @staticmethod
    def parse_args(args):
        return args[0] if args else '/'

class WhoamiCommand(BaseCommand):
    @staticmethod
    def run(command: str, *args) -> str:
        # Для whoami parse_args не нужен, просто возвращаем результат
        return os.getlogin()

    @staticmethod
    def parse_args(args):
        return []



class ClearCommand(BaseCommand):
    @staticmethod
    def run(command: str, *args) -> str:
        return ClearCommand.parse_args(args)

    @staticmethod
    def parse_args(args):
        return "clear"


class FindCommand(BaseCommand):
    @staticmethod
    def run(command: str, current_path: str, *args) -> str:
        # Вызов parse_args внутри run
        term = FindCommand.parse_args(args)
        if "Error" in term:
            return term  # Возвращаем сообщение об ошибке

        result = []
        for root, dirs, files in os.walk(current_path):
            for name in dirs + files:
                if term in name:
                    result.append(os.path.join(root, name))
        return '\n'.join(result) if result else f"find: no results for '{term}'"

    @staticmethod
    def parse_args(args):
        if len(args) < 1:
            return FindCommand.error("find: missing search term")
        return args[0]


# Диспетчер команд
class CommandDispatcher:
    def __init__(self):
        self.current_path = os.getcwd()  # Текущая директория
        self.commands = {
            'ls': LSCommand,
            'cd': CDCommand,
            'whoami': WhoamiCommand,
            'clear': ClearCommand,
            'find': FindCommand,
        }

    def execute(self, command: str) -> str:
        parts = command.split()
        if not parts:
            return ''

        cmd_name = parts[0]
        args = parts[1:]

        command_class = self.commands.get(cmd_name, None)
        if command_class:
            if cmd_name == 'cd':
                new_path = command_class.run(cmd_name, self.current_path, *args)
                if "Error" in new_path:
                    return new_path
                else:
                    self.current_path = new_path
                    return ""
            else:
                return command_class.run(cmd_name, self.current_path, *args)
        else:
            return f"{cmd_name}: command not found"
