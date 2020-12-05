# LeetCode题解(0158)：用Read4读取N个字符II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/read-n-characters-given-read4-ii-call-multiple-times/)（困难）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (74.71%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.cache = []
        self.size = 0
        self.finish = False

    def read(self, buf: List[str], n: int) -> int:
        while not self.finish and self.size < n:
            self.read4()

        length = min(self.size, n)
        self.size -= length
        buf[:length] = self.cache[:length]
        self.cache[:length] = []

        return length

    def read4(self):
        temp = [" "] * 4
        size = read4(temp)
        for i in range(size):
            self.cache.append(temp[i])
            self.size += 1
        if size < 4:
            self.finish = True
```