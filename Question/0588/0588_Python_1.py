from typing import List


class FileSystem:
    class Folder:
        def __init__(self):
            self.dir = {}
            self.file = {}

    class File:
        def __init__(self, content=""):
            self.content = content

    def __init__(self):
        self.root = self.Folder()

    def ls(self, path: str) -> List[str]:
        # 到达指定路径
        node = self.root
        path = [name for name in path.split("/") if name != ""]
        for name in path[:-1]:
            if name != "":
                if name not in node.dir:
                    return []
                node = node.dir[name]

        # 路径为文件夹
        if not path or (path and path[-1] in node.dir):
            if (path and path[-1] in node.dir):
                node = node.dir[path[-1]]

            # 遍历目标位置下的所有文件夹
            res = []
            for name in node.dir:
                res.append(name)
            for name in node.file:
                res.append(name)
            res.sort()
            return res

        # 路径为文件
        elif path[-1] in node.file:
            return [path[-1]]

    def mkdir(self, path: str) -> None:
        # 创建指定路径
        node = self.root
        for name in path.split("/"):
            if name != "":
                if name not in node.dir:
                    node.dir[name] = self.Folder()
                node = node.dir[name]

    def addContentToFile(self, filePath: str, content: str) -> None:
        # 创建指定路径
        node = self.root
        path = filePath.split("/")
        for name in path[:-1]:
            if name != "":
                if name not in node.dir:
                    node.dir[name] = self.Folder()
                node = node.dir[name]

        # 添加文件
        if path[-1] in node.file:
            node.file[path[-1]].content += content
        else:
            node.file[path[-1]] = self.File(content)

    def readContentFromFile(self, filePath: str) -> str:
        # 到达指定路径
        node = self.root
        path = filePath.split("/")
        for name in path[:-1]:
            if name != "":
                if name not in node.dir:
                    return ""
                node = node.dir[name]

        # 读取文件
        return node.file[path[-1]].content


if __name__ == "__main__":
    obj = FileSystem()
    print(obj.ls("/"))  # []
    obj.mkdir("/a/b/c")
    obj.addContentToFile("/a/b/c/d", "hello")
    print(obj.ls("/"))  # ["a"]
    print(obj.readContentFromFile("/a/b/c/d"))  # "hello"
