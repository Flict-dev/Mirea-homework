from abc import ABC
import re
from zipfile import ZipFile

class BaseCommand(ABC):
    @staticmethod
    def run(vfs, current_path, *args):
        pass

class LSCommand(BaseCommand):
    @staticmethod
    def run(vfs, current_path, *args):
        files = set()
        last_folder = current_path.split('/')[-2]
        for file_path in vfs.namelist():
            file_path = f"/{file_path}"
            if file_path.startswith(current_path):
                paths = file_path.split('/')
                files.add(paths[paths.index(last_folder) + 1])
        return '\n'.join([file for file in files if file])

class CDCommand(BaseCommand):
    @staticmethod
    def run(vfs, current_path, *args):
        if args[0] == "..":
            paths = [file for file in  current_path.split("/") if file]
            if len(paths) <= 1:
                return "/"
            paths.pop()
            return f"/{'/'.join(paths)}/"
        elif args[0] == "/":
            return "/"
        new_path = f"{current_path}{args[0]}" 
        for file_path in vfs.namelist():
            file_path = f"/{file_path}"
            if file_path.startswith(new_path):
                return f"{new_path}/"
        return "Error: path not found"
    
class ExitCommand(BaseCommand):
    @staticmethod
    def run(vfs, current_path, *args):
        return "exit"
    
class WhoamiCommand(BaseCommand):
    @staticmethod
    def run(vfs, current_path, *args):
        return "root"
    
class PWDCommand(BaseCommand):
    @staticmethod
    def run(vfs, current_path, *args):
        return current_path

class CommandDispatcher:
    def __init__(self, zip_path):
        self.zip_file = ZipFile(zip_path, 'r')
        self.current_path = '/'
        self.commands = {
            'ls': LSCommand,
            'cd': CDCommand,
            'exit': ExitCommand,
            'pwd': PWDCommand,
            'whoami': WhoamiCommand,
        }

    def execute(self, command: str) -> str:
        parts = command.split()
        cmd = parts[0]
        args = parts[1:]

        cmd_class = self.commands.get(cmd)

        if not cmd_class:
            return f"{cmd}: command not found"
        
        if cmd == "cd":
            result = cmd_class.run(self.zip_file, self.current_path, *args)
            if not result.startswith("Error:"):
                self.current_path = result
            return result
        return cmd_class.run(self.zip_file, self.current_path, *args)