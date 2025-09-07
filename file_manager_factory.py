from abc import ABC, abstractmethod

class FileManager(ABC):
    def __init__(self, filename):
        self.filename = filename
    @abstractmethod
    def edit(self):
        pass

class Json(FileManager):
    def edit(self):
        print(f"Editing JSON file {self.filename}.")
        data = {"New_key": {"New_value"}}
        print(f"Adding the Data: {data}")


class Xml(FileManager):
    def edit(self):
        print(f"Editing XML file {self.filename}.")
        print(f"Adding a new data!")

class  Txt(FileManager):
    def edit(self):
        print(f"Editing TXT file {self.filename}.")
        print("Adding a new text!")

class FileFactory:
    @staticmethod
    def create_file(file_type, filename):
        if file_type == "json":
            return Json(filename)
        elif file_type == "xml":
            return Xml(filename)
        elif file_type == "text":
            return Txt(filename)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

