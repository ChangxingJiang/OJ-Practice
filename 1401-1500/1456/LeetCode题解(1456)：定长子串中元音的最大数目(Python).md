# LeetCode题解(1456)：字符串的定长子串中元音的最大数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)（中等）

标签：字符串、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 108ms (99.89%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（滑动窗口）：

![LeetCode题解(1456)：截图](LeetCode题解(1456)：截图.png)

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # 处理字符串过短的情况
        if len(s) <= k:
            return s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")

        # 滑动窗口处理其他情况
        ans = num = s[:k].count("a") + s[:k].count("e") + s[:k].count("i") + s[:k].count("o") + s[:k].count("u")
        for i in range(len(s) - k):
            if s[i] in {"a", "e", "i", "o", "u"}:
                num -= 1
            if s[i + k] in {"a", "e", "i", "o", "u"}:
                num += 1
                ans = max(num, ans)
        return ans
```