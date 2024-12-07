import os
import time
from datetime import datetime
from abc import ABC, abstractmethod

class File(ABC):
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.extension = os.path.splitext(path)[1]
        self.creation_date = datetime.fromtimestamp(os.path.getctime(path))
        self.last_modified_date = datetime.fromtimestamp(os.path.getmtime(path))

    @abstractmethod
    def info(self):
        pass

class TextFile(File):
    def info(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            content = f.read()
        lines = content.splitlines()
        words = content.split()
        print(f"Text File: {self.name}\nLines: {len(lines)}\nWords: {len(words)}\nCharacters: {len(content)}")

class ImageFile(File):
    def info(self):
        # Placeholder for image dimensions (as we are not using external libraries)
        print(f"Image File: {self.name}\nDimensions: [Placeholder for dimensions]")

class CodeFile(File):
    def info(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            content = f.readlines()
        classes = sum(1 for line in content if line.strip().startswith('class '))
        methods = sum(1 for line in content if line.strip().startswith('def '))
        print(f"Code File: {self.name}\nLines: {len(content)}\nClasses: {classes}\nMethods: {methods}")

class DocumentChangeDetectionSystem:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.files = {}
        self.snapshot = {}

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        self.scan_folder()

    def scan_folder(self):
        current_files = os.listdir(self.folder_path)
        for filename in current_files:
            path = os.path.join(self.folder_path, filename)
            if os.path.isfile(path):
                self.files[filename] = self.create_file_object(path)

    def create_file_object(self, path):
        extension = os.path.splitext(path)[1].lower()
        if extension == '.txt':
            return TextFile(path)
        elif extension in ['.png', '.jpg']:
            return ImageFile(path)
        elif extension in ['.py', '.java']:
            return CodeFile(path)
        else:
            return File(path)

    def commit(self):
        self.snapshot = {name: os.path.getmtime(file.path) for name, file in self.files.items()}
        print("Snapshot committed.")

    def info(self, filename):
        file = self.files.get(filename)
        if file:
            file.info()
        else:
            print(f"File {filename} not found.")

    def status(self):
        current_files = os.listdir(self.folder_path)
        current_files_set = set(current_files)
        snapshot_files_set = set(self.snapshot.keys())

        for filename in current_files_set - snapshot_files_set:
            print(f"{filename} is a new file.")

        for filename in snapshot_files_set - current_files_set:
            print(f"{filename} was deleted.")

        for filename in current_files_set & snapshot_files_set:
            path = os.path.join(self.folder_path, filename)
            if os.path.getmtime(path) != self.snapshot[filename]:
                print(f"{filename} was modified.")
            else:
                print(f"{filename} is unchanged.")

if __name__ == "__main__":
    folder_path = "./monitor_folder"
    system = DocumentChangeDetectionSystem(folder_path)

    while True:
        command = input("Enter a command (commit/info/status/exit): ").strip().lower()
        if command == "commit":
            system.commit()
        elif command.startswith("info"):
            parts = command.split()
            if len(parts) > 1:
                system.info(parts[1])
            else:
                print("Please specify a file name.")
        elif command == "status":
            system.status()
        elif command == "exit":
            print("Exiting program.")
            break
        else:
            print("Unknown command.")
