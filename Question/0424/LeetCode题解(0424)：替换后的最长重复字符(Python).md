# LeetCode题解(0424)：替换后的最长重复字符(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-repeating-character-replacement/)（中等）

标签：滑动窗口、双指针、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 112ms (73.89%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.Counter()
        left = right = 0

        ans = 0

        while right < len(s):
            count[s[right]] += 1
            ans = max(ans, count[s[right]])

            # 窗口长度增长之后不会减少，一直保留最大值时的情况
            if (right - left + 1) - ans > k:
                count[s[left]] -= 1
                left += 1
            right += 1

        return right - left
```

