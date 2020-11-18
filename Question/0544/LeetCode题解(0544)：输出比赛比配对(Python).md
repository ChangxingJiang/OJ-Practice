# LeetCode题解(0544)：输出比赛比配对(Python)

题目：[原题链接](https://leetcode-cn.com/problems/output-contest-matches/)（中等）

标签：递归、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(NlogN)$ | 40ms (79.71%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（递归）：

```python
class Solution:
    def findContestMatch(self, n: int) -> str:
        return self.recursion([str(i) for i in range(1, n + 1)])

    def recursion(self, lst):
        size = len(lst)
        if size == 1:
            return lst[0]
        else:
            return self.recursion(["(" + lst[i] + "," + lst[size - i - 1] + ")" for i in range(size // 2)])
```