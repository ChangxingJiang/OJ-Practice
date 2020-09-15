# LeetCode题解(0919)：设计完全二叉树插入器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/complete-binary-tree-inserter/)（中等）

标签：树、二叉树、广度优先搜索、设计

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 100ms (20.69%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 76ms (80.00%)  |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.queue = collections.deque([root])
        while True:
            if self.queue[0].left:
                self.queue.append(self.queue[0].left)
            else:
                break
            if self.queue[0].right:
                self.queue.append(self.queue[0].right)
                self.queue.popleft()
            else:
                break

    def insert(self, v: int) -> int:
        if not self.queue[0].left:
            self.queue[0].left = TreeNode(v)
            self.queue.append(self.queue[0].left)
            return self.queue[0].val
        else:
            self.queue[0].right = TreeNode(v)
            self.queue.append(self.queue[0].right)
            return self.queue.popleft().val

    def get_root(self) -> TreeNode:
        return self.root
```

解法二（不再从列表中删除结点）：

```python
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.queue = [root]
        for node in self.queue:
            if node.left:
                self.queue.append(node.left)
            else:
                break
            if node.right:
                self.queue.append(node.right)
            else:
                break

    def insert(self, v: int) -> int:
        self.queue.append(TreeNode(v))
        idx, sub = divmod(len(self.queue), 2)
        if sub == 0:
            self.queue[idx - 1].left = self.queue[-1]
        else:
            self.queue[idx - 1].right = self.queue[-1]
        return self.queue[idx - 1].val

    def get_root(self) -> TreeNode:
        return self.queue[0]
```