# LeetCode题解(0933)：最近的请求次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-recent-calls/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | --         | --         | 344ms (74.43%) |
| Ans 2 (Python) | --         | --         | 376ms (42.68%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（使用数组实现）：

```python
class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.pop(0)
        return len(self.queue)
```

解法二（使用collections.deque实现）

```python
class RecentCounter:

    def __init__(self):
        self.queue = collections.deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)
```