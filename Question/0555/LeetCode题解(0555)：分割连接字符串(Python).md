# LeetCode题解(0555)：分割连接字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/split-concatenated-strings/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 68ms (72.58%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        lst = []
        for s in strs:
            if s > s[::-1]:
                lst.append(s)
            else:
                lst.append(s[::-1])

        ans = "".join(lst)

        for i, s in enumerate(lst):
            other = "".join(lst[i + 1:] + lst[:i])
            for j in range(len(s)):
                head = s[j:]
                tail = s[:j]
                ans = max(ans, head + other + tail, tail[::-1] + other + head[::-1])

        return ans
```