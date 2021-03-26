# LeetCode题解(0779)：第K个语法符号(Python)

题目：[原题链接](https://leetcode-cn.com/problems/k-th-symbol-in-grammar/)（中等）

标签：递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 32ms (93.91%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（递归）：

```python
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1 and K == 1:
            return 0
        elif K % 2 == 0:
            return 1 if not self.kthGrammar(N - 1, K // 2) else 0
        else:
            return 1 if self.kthGrammar(N - 1, K // 2 + 1) else 0
```