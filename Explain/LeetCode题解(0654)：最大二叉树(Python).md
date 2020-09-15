# LeetCode题解(0654)：依据数组生成符合指定条件的二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-binary-tree/)（中等）

标签：树、二叉树、深度优先搜索、栈

| 解法           | 时间复杂度                   | 空间复杂度 | 执行用时        |
| -------------- | ---------------------------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N×H)$ : 其中H为二叉树高度 | $O(N×H)$   | 308ms (15.82%)  |
| Ans 2 (Python) | $O(N)$                       | $O(H)$     | 208ms (100.00%) |
| Ans 3 (Python) |                              |            |                 |

解法一：

```python
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums:
            max_idx, max_val = -1, float("-inf")
            for i, n in enumerate(nums):
                if n > max_val:
                    max_val = n
                    max_idx = i
            root = TreeNode(max_val)
            root.left = self.constructMaximumBinaryTree(nums[:max_idx])
            root.right = self.constructMaximumBinaryTree(nums[max_idx + 1:])
            return root
```

解法二（优化解法一）：

![LeetCode题解(0654)：截图](LeetCode题解(0654)：截图.png)

```python
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        stack = []
        for n in nums:
            node = TreeNode(n)
            while stack and stack[-1].val < n:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)

        return stack[0]
```