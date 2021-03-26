# LeetCode题解(0395)：至少有K个重复字符的最长子串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/)（中等）

标签：递归、记忆化递归、分治算法、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(2^N)$   | $O(2^N)$   | 120ms (7.32%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    @functools.lru_cache(None)
    def longestSubstring(self, s: str, k: int, count=None, left=0, right=None) -> int:
        size = len(s)

        # 处理默认值变量
        if right is None:
            right = size - 1

        if count is None:
            count = [0] * 26
            for i in range(left, right + 1):
                count[ord(s[i]) - 97] += 1
        else:
            count = list(count)

        # 统计出现次数不足k的字符
        less_lst = set()
        for i, n in enumerate(count):
            if 0 < n < k:
                less_lst.add(i)

        # 移除开头多余字符
        while left <= right and (idx := ord(s[left]) - 97) in less_lst:
            count[idx] -= 1
            if count[idx] == 0:
                less_lst.remove(idx)
            left += 1

        # 移除结尾多余字符
        while left <= right and (idx := ord(s[right]) - 97) in less_lst:
            count[idx] -= 1
            if count[idx] == 0:
                less_lst.remove(idx)
            right -= 1

        # 处理字符串为空串的情况
        if left > right:
            return 0

        # 处理已经是目标字符串的情况
        if not less_lst:
            return right - left + 1

        # 递归处理两种可能
        count[ord(s[left]) - 97] -= 1
        v1 = self.longestSubstring(s, k, tuple(count), left + 1, right)
        count[ord(s[left]) - 97] += 1
        count[ord(s[right]) - 97] -= 1
        v2 = self.longestSubstring(s, k, tuple(count), left, right - 1)
        return max(v1, v2)
```