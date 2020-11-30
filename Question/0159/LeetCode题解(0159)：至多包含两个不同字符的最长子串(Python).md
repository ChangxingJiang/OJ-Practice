# LeetCode题解(0159)：至多包含两个不同字符的最长子串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters/)（中等）

标签：哈希表、双指针、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 88ms (28.13%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（滑动窗口）：

```python
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ans = 0
        size = len(s)
        left, right = 0, 0
        count = collections.Counter()
        while right < size:
            ch1 = s[right]
            count[ch1] += 1
            while len(count) > 2:
                ch2 = s[left]
                count[ch2] -= 1
                if count[ch2] == 0:
                    del count[ch2]
                left += 1
            right += 1
            ans = max(ans, right - left)
        return ans
```