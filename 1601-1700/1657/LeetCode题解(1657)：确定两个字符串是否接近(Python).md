# LeetCode题解(1657)：确定两个字符串是否接近(Python)

题目：[原题链接](https://leetcode-cn.com/problems/determine-if-two-strings-are-close/)（中等）

标签：贪心算法、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N1+N2)$ | $O(N1+N2)$ | 172ms (57.34%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1, count2 = Counter(word1), Counter(word2)
        return (len(word1) == len(word2) and
                set(count1.keys()) == set(count2.keys()) and
                set(count1.values()) == set(count2.values()))
```

