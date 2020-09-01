# LeetCode题解(1347)：将两个字符串制造为字母异位词的最小步骤数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/)（中等）

标签：字符串、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(S+T)$   | $O(S+T)$   | 324ms (30.74%) |
| Ans 2 (Python) | $O(S+T)$   | $O(S+T)$   | 128ms (82.68%) |
| Ans 3 (Python) |            |            |                |

解法一：

```
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # 统计t中的字符数量
        count = collections.Counter(t)

        # 统计s与t中字符差异数量
        for ch in s:
            if ch in count:
                count[ch] -= 1

        # 统计s比t多和少的字符数量
        much = 0
        less = 0
        for k, v in count.items():
            if v < 0:
                less -= v
            elif v > 0:
                much += v

        # 返回结果
        return max(much, less)
```

解法二：

```python
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # 统计s和t中的字符数量
        count1 = collections.Counter(s)
        count2 = collections.Counter(t)

        # 统计s与t中字符差异数量
        ans = 0
        for i in range(97, 124):
            ans += abs(count1[chr(i)] - count2[chr(i)])

        return ans // 2
```