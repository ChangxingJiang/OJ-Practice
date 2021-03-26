# LeetCode题解(Offer48)：寻找字符串中最长不含重复字符的子字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/)（中等）

标签：哈希表、双指针、移动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 104ms (22.40%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 60ms (97.85%)  |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        count = collections.Counter()
        last = 0
        for i, ch in enumerate(s):
            count[ch] += 1
            if count[ch] > 1:
                ans = max(ans, i - last)
                while count[ch] > 1 and last < i:
                    count[s[last]] -= 1
                    last += 1
        ans = max(ans, len(s) - last)

        return ans
```

解法二：

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        last_position = {}
        left = -1
        for right, ch in enumerate(s):
            if ch in last_position and last_position[ch] > left:
                ans = max(ans, right - left-1)
                left = last_position[ch]
                last_position[ch] = right
            else:
                last_position[ch] = right
        ans = max(ans, len(s) - left - 1)

        return ans

```