class Fancy:
    _MOD = 10 ** 9 + 7

    class Node:
        __slots__ = ["name", "val", "parent"]

        def __init__(self, name, val, parent=None):
            self.name = name  # 节点的类型
            self.val = val  # 节点的值
            self.parent = parent  # 节点的父节点

    def __init__(self):
        self.lst = []  # 叶节点列表
        self.top = []  # 根节点列表

    def append(self, val: int) -> None:
        node = self.Node(name="N", val=val)
        self.lst.append(node)
        self.top.append(node)

    def addAll(self, inc: int) -> None:
        root = self.Node(name="A", val=inc)
        for node in self.top:
            node.parent = root
        self.top = [root]

    def multAll(self, m: int) -> None:
        root = self.Node(name="M", val=m)
        for node in self.top:
            node.parent = root
        self.top = [root]

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.lst):
            return -1
        node = self.lst[idx]
        ans = node.val
        while node.parent:
            node = node.parent
            if node.name == "A":
                ans += node.val
            else:
                ans *= node.val
        return ans % self._MOD


if __name__ == "__main__":
    obj = Fancy()
    obj.append(2)
    obj.addAll(3)
    obj.append(7)
    obj.multAll(2)
    print("[RES]", obj.getIndex(0))  # 10
    obj.addAll(3)
    obj.append(10)
    obj.multAll(2)
    print("[RES]", obj.getIndex(0))  # 26
    print("[RES]", obj.getIndex(1))  # 34
    print("[RES]", obj.getIndex(2))  # 20
