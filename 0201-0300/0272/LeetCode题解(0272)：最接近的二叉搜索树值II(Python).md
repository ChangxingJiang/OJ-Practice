# LeetCode题解(0272)：最接近的二叉搜索树值II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/closest-binary-search-tree-value-ii/)（困难）

标签：树、二叉树、二叉搜索树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 36ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（中序遍历）：

```python
class Solution:
    def __init__(self):
        self.lst = []

    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        # 中序遍历二叉搜索树
        # O(N)
        self.inorder(root)

        # 二分查找目标值
        # O(logN)
        left = bisect.bisect_left(self.lst, target) - 1
        right = left + 1

        # 从目标值向两侧遍历寻找最接近的值
        # O(N)
        ans = []
        while len(ans) < k:
            if left >= 0 and right < len(self.lst):
                if target - self.lst[left] < self.lst[right] - target:
                    ans.append(self.lst[left])
                    left -= 1
                else:
                    ans.append(self.lst[right])
                    right += 1
            elif left >= 0:
                ans.append(self.lst[left])
                left -= 1
            elif right < len(self.lst):
                ans.append(self.lst[right])
                right += 1
            else:
                break

        return ans

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.lst.append(node.val)
            self.inorder(node.right)
```