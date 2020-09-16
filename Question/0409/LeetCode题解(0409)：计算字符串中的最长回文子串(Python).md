# LeetCode题解(0409)：计算字符串中的最长回文子串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-palindrome/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | O(n)       | 44ms (55.70%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def longestPalindrome(self, s: str) -> int:
    count = collections.Counter(s)
    has_odd = 0
    ans = 0
    for key, value in count.items():
        ans += (value // 2) * 2
        if has_odd == 0 and value % 2 != 0:
            has_odd = 1
    return ans + has_odd
```