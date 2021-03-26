# LeetCode题解(0170)：两数之和III(Python)

题目：[原题链接](https://leetcode-cn.com/problems/two-sum-iii-data-structure-design/)（简单）

标签：设计、哈希表

| 解法           | 时间复杂度                   | 空间复杂度 | 执行用时       |
| -------------- | ---------------------------- | ---------- | -------------- |
| Ans 1 (Python) | add = $O(1)$ ; find = $O(N)$ | $O(N)$     | 664ms (20.21%) |
| Ans 2 (Python) |                              |            |                |
| Ans 3 (Python) |                              |            |                |

解法一：

```python
class TwoSum:
    def __init__(self):
        self.count = collections.Counter()

    def add(self, number: int) -> None:
        self.count[number] += 1

    def find(self, value: int) -> bool:
        for x in self.count:
            y = value - x
            if x == y and self.count[x] >=2:
                return True
            if x != y and self.count[y] >=1:
                return True
        return False

```