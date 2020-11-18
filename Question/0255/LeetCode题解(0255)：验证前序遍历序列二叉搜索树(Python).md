# LeetCode题解(0255)：验证前序遍历序列二叉搜索树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/verify-preorder-sequence-in-binary-search-tree/)（中等）

标签：树、二叉树、二叉搜索树、栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(logN)$  | 76ms (85.43%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（栈）：

```python
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        find = float("-inf")
        stack = []
        for n in preorder:
            if n < find:
                return False
            elif not stack or n < stack[-1]:
                stack.append(n)
            else:
                while stack and n > stack[-1]:
                    find = max(find, stack.pop())
                stack.append(n)
        return True
```