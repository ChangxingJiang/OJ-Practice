# LeetCode题解：0155（最小栈）

题目：[题目链接](https://leetcode-cn.com/problems/min-stack/)（简单）

标签：栈、设计

| 解法           | 时间复杂度                                                   | 空间复杂度 | 执行用时        |
| :------------- | ------------------------------------------------------------ | ---------- | --------------- |
| Ans 1 (Python) | push = $O(1)$ ; pop = $O(1)$ ; top = $O(1)$ ; getMin = $O(logN)$ | $O(N)$     | 704ms (>20.85%) |
| Ans 2 (Python) | push = $O(1)$ ; pop = $O(logN)$ ; top = $O(1)$ ; getMin = $O(1)$ | $O(N)$     | 64ms (>99.65%)  |

解法一（使用Python的list直接实现，不符合题目要求）：

```python
class MinStack:

    def __init__(self):
        self.nums = []

    def push(self, x: int) -> None:
        self.nums.append(x)

    def pop(self) -> None:
        self.nums.pop(-1)

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return min(self.nums)
```

解法二（同时存储栈和最小值，符合题目要求）：

```python
class MinStack:

    def __init__(self):
        self.nums = []
        self.minimum = None

    def push(self, x: int) -> None:
        self.nums.append(x)
        if self.minimum is None or self.minimum > x:
            self.minimum = x

    def pop(self) -> None:
        x = self.nums.pop(-1)
        if self.minimum == x:
            if len(self.nums) >= 1:
                self.minimum = min(self.nums)
            else:
                self.minimum = None

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.minimum
```