# LeetCode题解(0157)：用Read4读取N个字符Python)

题目：[原题链接](https://leetcode-cn.com/problems/read-n-characters-given-read4/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (84.89%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def read(self, buf, n):
        now, remain = 0, n
        while True:
            cache = [" "] * 4
            size = read4(cache)
            for i in range(min(remain, size)):
                buf[now] = cache[i]
                now += 1
            remain -= size
            if size < 4 or remain <= 0:
                return now
```