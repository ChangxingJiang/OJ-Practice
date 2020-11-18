# LeetCode题解(0549)：二叉树中最长的连续序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence-ii/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 52ms (97.98%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.ans = 0

    def longestConsecutive(self, root: TreeNode) -> int:
        if root:
            self.dfs(root)

        return self.ans

    def dfs(self, node):
        # 返回值：递增序列开头、递增序列结尾、递减序列开头、递减序列结尾
        v = node.val

        if node.left and node.right:
            left1, left2, left3, left4 = self.dfs(node.left)
            right1, right2, right3, right4 = self.dfs(node.right)
            if v == left2 + 1 and v == right2 + 1:
                now1, now2 = min(left1, right1), v
            elif v == left2 + 1:
                now1, now2 = left1, v
            elif v == right2 + 1:
                now1, now2 = right1, v
            else:
                now1, now2 = v, v
            if v == left3 - 1 and v == right3 - 1:
                now3, now4 = v, max(left4, right4)
            elif v == left3 - 1:
                now3, now4 = v, left4
            elif v == right3 - 1:
                now3, now4 = v, right4
            else:
                now3, now4 = v, v

        elif node.left:
            left1, left2, left3, left4 = self.dfs(node.left)
            if v == left2 + 1:
                now1, now2 = left1, v
            else:
                now1, now2 = v, v
            if v == left3 - 1:
                now3, now4 = v, left4
            else:
                now3, now4 = v, v

        elif node.right:
            right1, right2, right3, right4 = self.dfs(node.right)
            if v == right2 + 1:
                now1, now2 = right1, v
            else:
                now1, now2 = v, v
            if v == right3 - 1:
                now3, now4 = v, right4
            else:
                now3, now4 = v, v

        else:
            now1, now2, now3, now4 = v, v, v, v

        # 计算长度最大值
        len1 = now2 - now1 + 1
        len2 = now4 - now3 + 1
        len3 = len1 + len2 - 1 if now2 == now3 else 0
        self.ans = max(self.ans, len1, len2, len3)

        return now1, now2, now3, now4
```