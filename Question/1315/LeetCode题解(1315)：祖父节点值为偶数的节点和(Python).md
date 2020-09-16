# LeetCode题解(1315)：计算二叉树中祖父节点值为偶数的节点和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sum-of-nodes-with-even-valued-grandparent/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 124ms (59.48%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def sumEvenGrandparent(self, root: TreeNode, father=None, grandfather=None) -> int:
        if not root:
            return 0

        # 累计当前节点
        ans = 0
        if grandfather and grandfather.val % 2 == 0:
            ans += root.val

        grandfather = father
        father = root
        ans += self.sumEvenGrandparent(root.left, father, grandfather)
        ans += self.sumEvenGrandparent(root.right, father, grandfather)

        return ans
```