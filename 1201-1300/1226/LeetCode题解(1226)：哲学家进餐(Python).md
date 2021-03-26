# LeetCode题解(1226)：哲学家进餐(Python)

题目：[原题链接](https://leetcode-cn.com/problems/the-dining-philosophers/)（中等）

标签：多线程

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 84ms (46.90%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（每个时间只能有一个人吃）：

```python
import threading


class DiningPhilosophers:

    def __init__(self):
        self.lock = threading.Lock()

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        self.lock.acquire()
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        self.lock.release()
```



