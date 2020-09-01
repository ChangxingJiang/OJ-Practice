# LeetCode题解(1422)：分割字符串的最大得分(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-score-after-splitting-a-string/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 48ms (56.27%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 40ms (87.75%) |
| Ans 3 (Python) |            |            |               |

解法一（暴力解法）：

```python
def maxScore(self, s: str) -> int:
    ans = 0
    for i in range(1, len(s)):
        ans = max(ans, s[0:i].count("0") + s[i:].count("1"))
    return ans
```

解法二（两次遍历）：

```python
def maxScore(self, s: str) -> int:
    a = 0
    for c in s:
        if c == "1":
            a += 1

    ans = 0

    b = 0
    for c in s[:-1]:
        if c == "0":
            b += 1
            ans = max(ans, a + b)
        else:
            a -= 1
            ans = max(ans, a + b)

    return ans
```