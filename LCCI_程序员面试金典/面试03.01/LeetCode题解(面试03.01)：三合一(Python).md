# LeetCode题解(面试03.01)：用一个数组实现三个栈(Python)

题目：[原题链接](https://leetcode-cn.com/problems/three-in-one-lcci/submissions/)（简单）

标签：设计、栈

| 解法           | 时间复杂度        | 空间复杂度 | 执行用时       |
| -------------- | ----------------- | ---------- | -------------- |
| Ans 1 (Python) | 所有方法 : $O(1)$ | $O(N)$     | 164ms (90.85%) |
| Ans 2 (Python) |                   |            |                |
| Ans 3 (Python) |                   |            |                |

解法一：

```python
class TripleInOne:

    def __init__(self, stackSize: int):
        self.size = stackSize
        self.lst = [-1] * (self.size * 3)
        self.idx = [0, self.size, self.size * 2]  # 头结点
        self.length = [0, 0, 0]  # 当前长度

    def push(self, stackNum: int, value: int) -> None:
        if self.length[stackNum] < self.size:
            self.lst[self.idx[stackNum] + self.length[stackNum]] = value
            self.length[stackNum] += 1

    def pop(self, stackNum: int) -> int:
        if not self.isEmpty(stackNum):
            val = self.lst[self.idx[stackNum] + self.length[stackNum] - 1]
            self.length[stackNum] -= 1
            return val
        else:
            return -1

    def peek(self, stackNum: int) -> int:
        if not self.isEmpty(stackNum):
            return self.lst[self.idx[stackNum] + self.length[stackNum] - 1]
        else:
            return -1

    def isEmpty(self, stackNum: int) -> bool:
        return self.length[stackNum] == 0
```