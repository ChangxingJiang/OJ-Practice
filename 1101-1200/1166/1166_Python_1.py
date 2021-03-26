class FileSystem:

    def __init__(self):
        self.hashmap = {"": -1}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.hashmap:
            return False
        if path[:path.rindex("/")] not in self.hashmap:
            return False
        self.hashmap[path] = value
        return True

    def get(self, path: str) -> int:
        if path in self.hashmap:
            return self.hashmap[path]
        else:
            return -1


if __name__ == "__main__":
    obj = FileSystem()
    print(obj.createPath("/a", 1))  # True
    print(obj.get("/a"))  # 1
    print()

    obj = FileSystem()
    print(obj.createPath("/leet", 1))  # True
    print(obj.createPath("/leet/code", 2))  # True
    print(obj.get("/leet/code"))  # 2
    print(obj.createPath("/c/d", 1))  # False
    print(obj.get("/c"))  # -1
    print()
