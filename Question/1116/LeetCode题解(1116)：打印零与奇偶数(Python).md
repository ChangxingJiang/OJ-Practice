# LeetCode题解(1116)：打印零与奇偶数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/print-zero-even-odd/)（中等）

标签：多线程

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 64ms (31.07%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```mysql
import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.s1 = threading.Semaphore(1)
        self.s2 = threading.Semaphore(0)
        self.s3 = threading.Semaphore(0)

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.s1.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.s2.release()
            else:
                self.s3.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 2 == 0:
                self.s2.acquire()
                printNumber(i)
                self.s1.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 2 == 1:
                self.s3.acquire()
                printNumber(i)
                self.s1.release()
```