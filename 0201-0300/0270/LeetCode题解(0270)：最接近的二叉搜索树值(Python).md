# LeetCode题解(0270)：最接近的二叉搜索树值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/closest-binary-search-tree-value/)（简单）

标签：树、二叉树、二叉搜索树、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 44ms (94.12%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        smaller, bigger = float("-inf"), float("inf")
        while root:
            if root.val < target:
                smaller = root.val
                root = root.right
            elif target < root.val:
                bigger = root.val
                root = root.left
            else:
                return int(target)

        if bigger - target > target - smaller:
            return smaller
        else:
            return bigger
```

