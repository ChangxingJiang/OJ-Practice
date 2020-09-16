# LeetCode题解(1381)：设计一个支持增量操作的栈(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-a-stack-with-increment-operation/)（中等）

标签：栈

| 解法           | 时间复杂度                                        | 空间复杂度 | 执行用时       |
| -------------- | ------------------------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | push = $O(1)$ ; pop = $O(1)$ ; increment = $O(K)$ | $O(N)$     | 144ms (72.34%) |
| Ans 2 (Python) |                                                   |            |                |
| Ans 3 (Python) |                                                   |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.stack), k)):
            self.stack[i] += val
```