# LeetCode题解(0099)：在不改变二叉树结构的前提下恢复乱序的二叉搜索树的顺序(Python)

题目：[原题链接](https://leetcode-cn.com/problems/recover-binary-search-tree/)（困难）

标签：数、二叉树、二叉搜索树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 88ms (82.39%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 124ms (6.91%) |
| Ans 3 (Python) | $O(N)$     | $O(H)$     | 92ms (67.15%) |

解法一（两次遍历并排序的暴力解法）：

```python
class Solution:
    def __init__(self):
        self.idx = 0

    def recoverTree(self, root: TreeNode) -> None:
        # 中序遍历二叉树并排序元素
        def recursor_get(node):
            if node:
                return recursor_get(node.left) + [node.val] + recursor_get(node.right)
            else:
                return []

        lst = recursor_get(root)
        lst.sort()

        # 中序遍历二叉树并填写有序元素
        def recursor_update(node):
            if node:
                recursor_update(node.left)
                node.val = lst[self.idx]
                self.idx += 1
                recursor_update(node.right)

        recursor_update(root)
```

解法二（显式中序遍历）：

```python
class Solution:
    def __init__(self):
        self.idx = 0

    def recoverTree(self, root: TreeNode) -> None:
        # 中序遍历二叉树
        def recursor_get(node):
            if node:
                return recursor_get(node.left) + [node.val] + recursor_get(node.right)
            else:
                return []

        # 寻找需要被交换的两个节点
        lst = recursor_get(root)
        x, y = None, None
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                if not x:
                    x = lst[i]
                y = lst[i + 1]

        if x is None or y is None:
            return

        # 中序遍历二叉树并调换指定顺序
        def recursor_update(node):
            if node:
                recursor_update(node.left)

                # 调整当前值
                if node.val == x:
                    node.val = y
                elif node.val == y:
                    node.val = x

                recursor_update(node.right)

        recursor_update(root)
```

解法三（隐式中序遍历）：

```python
class Solution:
    def __init__(self):
        self.idx = 0
        self.x = None
        self.y = None
        self.last = None

    def recoverTree(self, root: TreeNode) -> None:
        # 中序遍历二叉树并寻找顺序错误的位置
        def recursor_get(node):
            if node:
                recursor_get(node.left)
                if self.last and self.last.val >= node.val:
                    if not self.x:
                        self.x = self.last
                    self.y = node
                self.last = node
                recursor_get(node.right)

        recursor_get(root)

        # 交换两个点
        if self.x and self.y:
            self.x.val, self.y.val = self.y.val, self.x.val
```



