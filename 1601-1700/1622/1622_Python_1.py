class Fancy:
    _MOD = 10 ** 9 + 7

    class Node:
        __slots__ = ["name", "idx", "val", "children"]

        def __init__(self, name, idx, val, children=None):
            if children is None:
                children = []

            self.name = name  # 节点类型
            self.idx = idx  # 节点最小下标
            self.val = val  # 节点的值
            self.children = children  # 节点的子节点

        def __repr__(self):
            return str(self.idx)

    def __init__(self):
        self.lst = []
        self.i = 0

    def append(self, val: int) -> None:
        self.lst.append(self.Node(name="N", idx=self.i, val=val))
        self.i += 1

    def addAll(self, inc: int) -> None:
        self.lst = [self.Node(name="A", idx=0, val=inc, children=self.lst)]

    def multAll(self, m: int) -> None:
        self.lst = [self.Node(name="M", idx=0, val=m, children=self.lst)]

    def getIndex(self, idx: int) -> int:
        if idx < self.i:
            return self._dfs(idx, self.lst) % self._MOD
        else:
            return -1

    def _dfs(self, idx, lst):
        # 在列表中寻找目标坐标节点
        l, r = 0, len(lst)
        while l < r:
            m = (l + r) // 2
            if lst[m].idx <= idx:
                l = m + 1
            else:
                r = m
        node = lst[r - 1]

        # 处理不同类型的节点
        if node.name == "N":
            # print(node.val)
            return node.val
        elif node.name == "A":
            res = self._dfs(idx, node.children)
            # print(res, "+", node.val)
            return res + node.val
        else:
            res = self._dfs(idx, node.children)
            # print(res, "*", node.val)
            return res * node.val


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
