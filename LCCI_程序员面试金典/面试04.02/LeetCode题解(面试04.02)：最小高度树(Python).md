# LeetCode题解(面试04.02)：生成高度最小的二叉搜索树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-height-tree-lcci/)（简单）

标签：树、二叉树、二叉搜索树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (96.68%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int], left=None, right=None) -> TreeNode:
        if left is None:
            left = 0
        if right is None:
            right = len(nums) - 1

        # 处理只有一个节点的情况
        if left > right:
            return None

        elif left == right:
            return TreeNode(nums[left])

        # 处理有更多节点的情况
        else:
            mid = (left + right) // 2
            head = TreeNode(nums[mid])
            head.left = self.sortedArrayToBST(nums, left=left, right=mid - 1)
            head.right = self.sortedArrayToBST(nums, left=mid + 1, right=right)
            return head
```