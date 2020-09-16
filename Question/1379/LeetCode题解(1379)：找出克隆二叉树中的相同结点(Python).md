# LeetCode题解(1379)：找出指定节点在克隆二叉树中的相同节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)（中等）

标签：树、二叉树、深度优先搜索、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 820ms (20.17%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 668ms (99.72%) |
| Ans 3 (Python) |            |            |                |

解法一（深度优先搜索）：

```python
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        if target is original:
            return cloned
        return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)
```

解法二（广度优先搜索）：

![LeetCode题解(1379)：截图](LeetCode题解(1379)：截图.png)

```python
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original:
            queue = collections.deque([cloned])
            while queue:
                node = queue.popleft()
                if node.val == target.val:
                    return node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
```