# LeetCode题解(面试08.09)：括号(Python)

题目：[原题链接](https://leetcode-cn.com/problems/bracket-lcci/)（中等）

标签：回溯算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(2^N)$   | $O(2^N)$   | 48ms (39.53%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def generateParenthesis(self, n: int, left: int = 0) -> List[str]:
        self.now = []
        self.ans = []

        def count(l, r):
            if l == r:
                self.now.append("(")
                count(l + 1, r)
                self.now.pop()
            elif l == n:
                self.ans.append("".join(self.now + [")"] * (l - r)))
            else:
                self.now.append("(")
                count(l + 1, r)
                self.now.pop()
                self.now.append(")")
                count(l, r + 1)
                self.now.pop()

        count(l=0, r=0)

        return self.ans
```