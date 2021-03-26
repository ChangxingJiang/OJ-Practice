# LeetCode题解(1115)：交替打印FooBar(Python)

题目：[原题链接](https://leetcode-cn.com/problems/print-foobar-alternately/)（中等）

标签：多线程

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 64ms (57.75%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class FooBar:
    def __init__(self, n):
        self.n = n
        self.s1 = threading.Semaphore(1)
        self.s2 = threading.Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.s1.acquire()
            printFoo()
            self.s2.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.s2.acquire()
            printBar()
            self.s1.release()
```