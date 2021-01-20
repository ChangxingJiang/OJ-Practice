# LeetCode题解(1208)：尽可能使字符串相等(Python)

题目：[原题链接](https://leetcode-cn.com/problems/get-equal-substrings-within-budget/)（中等）

标签：数组、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 80ms (92.68%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        size = len(s)

        lst = []
        for i in range(size):
            lst.append(abs(ord(s[i]) - ord(t[i])))

        ans = 0

        left = 0
        cost = 0
        for right in range(size):
            cost += lst[right]
            right += 1
            while cost > maxCost:
                cost -= lst[left]
                left += 1
            ans = max(ans, right - left)

        return ans
```

