# LeetCode题解(1446)：计算最长连续字符的子串长度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/consecutive-characters/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 52ms (76.53%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（双指针）：

```python
def maxPower(self, s: str) -> int:
    last = s[0]
    start = 0
    ans = 0
    for i in range(1, len(s)):
        if s[i] != last:
            ans = max(ans, i - start)
            last = s[i]
            start = i
    else:
        ans = max(ans, len(s) - start)

    return ans
```