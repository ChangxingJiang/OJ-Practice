# LeetCode题解(1622)：奇妙序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/fancy-sequence/)（困难）

标签：数学、设计、线段树

| 解法           | 时间复杂度                                                   | 空间复杂度 | 执行用时       |
| -------------- | ------------------------------------------------------------ | ---------- | -------------- |
| Ans 1 (Python) | append = $O(1)$ ; addAll = $O(1)$ ; multAll = $O(1)$ ; getIndex = $O(N)$ | $O(N)$     | 超出时间限制   |
| Ans 2 (Python) | append = $O(1)$ ; addAll = $O(1)$ ; multAll = $O(1)$ ; getIndex = $O(logN)$ | $O(N)$     | 972ms (83.03%) |
| Ans 3 (Python) |                                                              |            |                |

解法一（暴力解法）：

```python
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
```

解法二（乘法逆元压缩）：

```python
class Fancy:
    _MOD = 10 ** 9 + 7

    def __init__(self):
        self.num = []  # 数值列表
        self.operate = [[1, 0]]  # 操作列表

    def append(self, val: int) -> None:
        self.num += [val]
        self.operate += [self.operate[-1]]

    def addAll(self, inc: int) -> None:
        self.operate[-1] = [self.operate[-1][0], self.operate[-1][1] + inc]

    def multAll(self, m: int) -> None:
        self.operate[-1] = [self.operate[-1][0] * m % self._MOD, self.operate[-1][1] * m % self._MOD]

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.num):
            return -1
        a1, b1 = self.operate[-1]
        a2, b2 = self.operate[idx]
        inv = pow(a2, self._MOD - 2, self._MOD)
        return ((self.num[idx] * a1 + a2 * b1 - a1 * b2) * inv) % self._MOD
```