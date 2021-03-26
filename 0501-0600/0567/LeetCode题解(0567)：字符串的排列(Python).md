# LeetCode题解(0567)：字符串的排列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/permutation-in-string/)（中等）

标签：数组、双指针、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(S1+S2)$ | $O(S1)$    | 100ms (41.36%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need, window = collections.Counter(s1), collections.Counter()
        count = 0

        i1 = i2 = 0
        while i2 < len(s2):
            ch2 = s2[i2]
            i2 += 1

            if ch2 in need:
                window[ch2] += 1
                if window[ch2] == need[ch2]:
                    count += 1

            while i2 - i1 >= len(s1):
                if count == len(need):
                    return True

                ch1 = s2[i1]
                i1 += 1

                if ch1 in window:
                    if window[ch1] == need[ch1]:
                        count -= 1
                    window[ch1] -= 1

        return False
```

