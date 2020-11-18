# LeetCode题解(1593)：拆分字符串使唯一子字符串的数目最大(Python)

题目：[原题链接](https://leetcode-cn.com/problems/split-a-string-into-the-max-number-of-unique-substrings/)（中等）

标签：回溯算法、字符串、递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(2^N×N)$ | $O(N)$     | 356ms (70%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def __init__(self):
        self.max = 0

    def maxUniqueSplit(self, s: str) -> int:

        # @functools.lru_cache
        def recursor(ss: str, val, now):
            # print(ss, val, now)

            if not ss:
                self.max = max(self.max, val)
                return

            if ss not in now:
                self.max = max(self.max, val + 1)

            for i in range(1, len(ss)):
                if ss[:i] not in now:
                    now.add(ss[:i])
                    recursor(ss[i:], val + 1, now.copy())
                    now.remove(ss[:i])

        recursor(s, 0, set())

        return self.max
```