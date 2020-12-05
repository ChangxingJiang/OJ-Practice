from typing import List


class FileSystem:

    def __init__(self):
        pass

    def ls(self, path: str) -> List[str]:
        pass

    def mkdir(self, path: str) -> None:
        pass

    def addContentToFile(self, filePath: str, content: str) -> None:
        pass

    def readContentFromFile(self, filePath: str) -> str:
        pass


if __name__ == "__main__":
    obj = FileSystem()
    print(obj.ls("/"))  # []
    obj.mkdir("/a/b/c")
    obj.addContentToFile("/a/b/c/d", "hello")
    print(obj.ls("/"))  # ["a"]
    print(obj.readContentFromFile("/a/b/c/d"))  # "hello"
