# code_editor.py

class CodeEditor:
    def __init__(self) -> None:
        self.content = ""

    def open_file(self, filepath: str) -> None:
        with open(filepath, 'r') as file:
            self.content = file.read()
        print(f"Opened file {filepath}")

    def save_file(self, filepath: str) -> None:
        with open(filepath, 'w') as file:
            file.write(self.content)
        print(f"Saved file {filepath}")