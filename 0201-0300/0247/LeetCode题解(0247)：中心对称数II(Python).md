# LeetCode题解(0247)：中心对称数II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/strobogrammatic-number-ii/)（中等）

标签：数学、递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(10^N)$  | $O(10^N)$  | 164ms (8.93%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（递归）：

```python
class Solution:
    def __init__(self):
        self.reverse_lst = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }
        self.ans = []

    def findStrobogrammatic(self, n: int) -> List[str]:
        self.count(n, "")
        return self.ans

    def count(self, n: int, now: str, first: bool = True):
        if n == 0:
            self.ans.append(now)
        elif n <= len(now):
            self.count(n - 1, now + self.reverse_lst[now[n - 1]], first=False)
        elif n == 1 or n == len(now) + 1:
            for num in ["0", "1", "8"]:
                self.count(n - 1, now + num, first=False)
        else:
            if first:
                lst = ["1", "6", "8", "9"]
            else:
                lst = ["0", "1", "6", "8", "9"]
            for num in lst:
                self.count(n - 1, now + num, first=False)
```