# LeetCode题解(1305)：排序两棵二叉搜索树中的所有元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees/)（中等）

标签：树、二叉树、二叉搜索树、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N1+N2)$ | $O(1)$     | 356ms (97.95%) |
| Ans 2 (Python) | $O(N1+N2)$ | $O(1)$     | 372ms (90.64%) |
| Ans 3 (Python) |            |            |                |

解法一（迭代器实现）：

```python
def inorder_traversal_to_iter(node):
    stack = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            yield node.val
            node = node.right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # 生成两棵二叉搜索树的中序遍历迭代器
        lst1 = inorder_traversal_to_iter(root1)
        lst2 = inorder_traversal_to_iter(root2)

        ans = []
        val1 = next(lst1) if root1 else None
        val2 = next(lst2) if root2 else None

        if val1 is not None and val2 is not None:
            while True:
                if val1 <= val2:
                    ans.append(val1)
                    try:
                        val1 = next(lst1)
                    except StopIteration:
                        try:
                            while True:
                                ans.append(val2)
                                val2 = next(lst2)
                        except StopIteration:
                            break
                else:
                    ans.append(val2)
                    try:
                        val2 = next(lst2)
                    except StopIteration:
                        try:
                            while True:
                                ans.append(val1)
                                val1 = next(lst1)
                        except StopIteration:
                            break
        elif val1 is None:
            try:
                while True:
                    ans.append(val2)
                    val2 = next(lst2)
            except StopIteration:
                pass
        elif val2 is None:
            try:
                while True:
                    ans.append(val1)
                    val1 = next(lst1)
            except StopIteration:
                pass
        return ans
```

解法二（简化解法一逻辑）：

```python
def inorder_traversal_to_iter(node):
    stack = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            yield node.val
            node = node.right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # 生成两棵二叉搜索树的中序遍历迭代器
        lst1 = inorder_traversal_to_iter(root1)
        lst2 = inorder_traversal_to_iter(root2)

        ans = []
        val1 = None
        val2 = None

        while True:
            if val1 is None:
                try:
                    val1 = next(lst1)
                except StopIteration:
                    try:
                        while True:
                            if val2 is not None:
                                ans.append(val2)
                            val2 = next(lst2)
                    except StopIteration:
                        break
            if val2 is None:
                try:
                    val2 = next(lst2)
                except StopIteration:
                    try:
                        while True:
                            ans.append(val1)
                            val1 = next(lst1)
                    except StopIteration:
                        break
            if val1 <= val2:
                ans.append(val1)
                val1 = None
            else:
                ans.append(val2)
                val2 = None

        return ans
```