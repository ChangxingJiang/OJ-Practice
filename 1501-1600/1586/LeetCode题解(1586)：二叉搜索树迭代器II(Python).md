# LeetCode题解(1586)：二叉搜索树迭代器II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-search-tree-iterator-ii/)（中等）

标签：设计、树、二叉树、二叉搜索树、栈

| 解法           | 时间复杂度           | 空间复杂度 | 执行用时       |
| -------------- | -------------------- | ---------- | -------------- |
| Ans 1 (Python) | 每个操作 : $O(logN)$ | $O(logN)$  | 516ms (87.50%) |
| Ans 2 (Python) |                      |            |                |
| Ans 3 (Python) |                      |            |                |

解法一（栈维护父节点栈）：

```python
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.start = False
        self.parent = []
        self.now = None

    def hasNext(self) -> bool:
        if not self.start:
            return True
        else:
            if self.now.right:
                return True
            else:
                val = self.now.val
                for parent in self.parent:
                    if parent.val > val:
                        return True
                    if parent.right and parent.right.val > val:
                        return True
                return False

    def next(self) -> int:
        if self.start:
            if self.now.right:
                self.parent.append(self.now)
                self.now = self.now.right
                while self.now.left:
                    self.parent.append(self.now)
                    self.now = self.now.left
                return self.now.val
            else:
                val = self.now.val
                while self.parent:
                    self.now = self.parent.pop()
                    if self.now.val > val:
                        return self.now.val
                    if self.now.right and self.now.right.val > val:
                        self.parent.append(self.now)
                        self.now = self.now.right
                        while self.now.left:
                            self.parent.append(self.now)
                            self.now = self.now.left
                        return self.now.val
                return None
        else:
            self.start = True
            self.now = self.root
            while self.now.left:
                self.parent.append(self.now)
                self.now = self.now.left
            return self.now.val

    def hasPrev(self) -> bool:
        if not self.start:
            return False
        elif self.now.left:
            return True
        else:
            val = self.now.val
            for parent in self.parent:
                if parent.val < val:
                    return True
                if parent.left and parent.left.val < val:
                    return True
            return False

    def prev(self) -> int:
        if self.now.left:
            self.parent.append(self.now)
            self.now = self.now.left
            while self.now.right:
                self.parent.append(self.now)
                self.now = self.now.right
            return self.now.val
        else:
            val = self.now.val
            while self.parent:
                self.now = self.parent.pop()
                if self.now.val < val:
                    return self.now.val
                if self.now.left and self.now.left.val < val :
                    self.parent.append(self.now)
                    self.now = self.now.left
                    while self.now.right:
                        self.parent.append(self.now)
                        self.now = self.now.right
                    return self.now.val
```