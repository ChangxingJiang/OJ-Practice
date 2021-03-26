# LeetCode题解(0173)：二叉搜索迭代器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-search-tree-iterator/)（中等）

标签：树、二叉树、二叉树-遍历、二叉搜索树、栈、设计

相关题目：0094（实际上就是二叉搜索树的中序遍历）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(logN)$  | 116ms (40.10%) |
| Ans 2 (Python) | $O(N)$     | $O(logN)$  | 104ms (81.09%) |
| Ans 3 (Python) | $O(N)$     | $O(logN)$  | 96ms (96.38%)  |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（初始化完成中序遍历）：

```python
class BSTIterator:

    def __init__(self, root: TreeNode):
        stack = [root]
        self.ans = []
        while stack:
            node = stack[-1]
            if node:
                stack.append(node.left)
            else:
                stack.pop()
                if not stack:
                    break
                now = stack.pop()
                self.ans.append(now.val)
                stack.append(now.right)

    def next(self) -> int:
        return self.ans.pop(0)

    def hasNext(self) -> bool:
        return len(self.ans) > 0
```

解法二（解法一的优化）：

```python
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = [root]

    def next(self) -> int:
        while self.stack:
            node = self.stack[-1]
            if node:
                self.stack.append(node.left)
            else:
                self.stack.pop()
                if not self.stack:
                    break
                now = self.stack.pop()
                self.stack.append(now.right)
                return now.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0 and self.stack[0] is not None
```

解法三：

```python
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        ans = node.val
        node = node.right
        while node:
            self.stack.append(node)
            node = node.left
        return ans

    def hasNext(self) -> bool:
        return len(self.stack) > 0 and self.stack[0] is not None
```