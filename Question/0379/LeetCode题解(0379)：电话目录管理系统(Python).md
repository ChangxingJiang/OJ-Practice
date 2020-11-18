# LeetCode题解(0379)：电话目录管理系统(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-phone-directory/)（中等）

标签：设计、集合、哈希表

| 解法           | 时间复杂度                                       | 空间复杂度 | 执行用时       |
| -------------- | ------------------------------------------------ | ---------- | -------------- |
| Ans 1 (Python) | get = $O(1)$ ; check = $O(1)$ ; release = $O(1)$ | $O(N)$     | 108ms (85.94%) |
| Ans 2 (Python) |                                                  |            |                |
| Ans 3 (Python) |                                                  |            |                |

解法一（集合）：

```python
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.pool = {i for i in range(maxNumbers)}

    def get(self) -> int:
        if self.pool:
            return self.pool.pop()
        else:
            return -1

    def check(self, number: int) -> bool:
        return number in self.pool

    def release(self, number: int) -> None:
        self.pool.add(number)
```