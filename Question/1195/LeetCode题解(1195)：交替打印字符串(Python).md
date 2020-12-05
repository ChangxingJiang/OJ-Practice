# LeetCode题解(1195)：交替打印字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/fizz-buzz-multithreaded/)（中等）

标签：多线程

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (67.39%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
import threading


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.lock = threading.Semaphore(1)
        self.s3 = threading.Semaphore(0)
        self.s5 = threading.Semaphore(0)
        self.s15 = threading.Semaphore(0)

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 != 0:
                self.s3.acquire()
                printFizz()
                self.lock.release()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 != 0 and i % 5 == 0:
                self.s5.acquire()
                printBuzz()
                self.lock.release()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 == 0:
                self.s15.acquire()
                printFizzBuzz(i)
                self.lock.release()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.lock.acquire()
            if i % 3 == 0 and i % 5 == 0:
                self.s15.release()
            elif i % 3 == 0:
                self.s3.release()
            elif i % 5 == 0:
                self.s5.release()
            else:
                printNumber(i)
                self.lock.release()
```