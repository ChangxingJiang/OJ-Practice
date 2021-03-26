# LeetCode题解(1117)：H2O生成(Python)

题目：[原题链接](https://leetcode-cn.com/problems/building-h2o/)（中等）

标签：多线程

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 56ms (33.33%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class H2O:
    def __init__(self):
        self.count = 0
        self.s1 = threading.Semaphore(2)
        self.s2 = threading.Semaphore(0)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.s1.acquire()
        releaseHydrogen()
        self.count += 1
        if self.count == 2:
            self.s2.release()
            self.count = 0

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.s2.acquire()
        releaseOxygen()
        self.s1.release()
        self.s1.release()
```