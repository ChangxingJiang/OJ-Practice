# LeetCode题解(0199)：计算二叉树的右视图(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-tree-right-side-view/)（中等）

标签：树、二叉树、深度优先搜索、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(H)$     | 48ms (31.80%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 40ms (81.32%) |
| Ans 3 (Python) |            |            |               |

解法一（深度优先搜索）：

```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # 处理特殊情况
        if not root:
            return []

        # 处理一般情况
        ans = [root.val]
        stack = [(root, 0)]
        while stack:
            node, level = stack[-1]
            if node.right:
                stack.append((node.right, level + 1))
                if level + 1 == len(ans):
                    ans.append(node.right.val)
            else:
                while stack:
                    node, level = stack.pop()
                    if node.left:
                        stack.append((node.left, level + 1))
                        if level + 1 == len(ans):
                            ans.append(node.left.val)
                        break
        return ans
```

解法二（广度优先搜索）：

```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # 处理特殊情况
        if not root:
            return []

        # 处理一般情况
        ans = [root.val]
        now_node = [root]
        while now_node:
            node_most_right = None
            next_node = []
            for node in now_node:
                if node.right:
                    next_node.append(node.right)
                    if not node_most_right:
                        node_most_right = node.right
                if node.left:
                    next_node.append(node.left)
                    if not node_most_right:
                        node_most_right = node.left
            if next_node:
                ans.append(node_most_right.val)
            now_node = next_node

        return ans
```