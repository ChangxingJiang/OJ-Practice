# LeetCode题解(1638)：统计两字符串中只差一个字符的子串数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-substrings-that-differ-by-one-character/)（中等）

标签：字符串、哈希表、字典树

| 解法           | 时间复杂度    | 空间复杂度 | 执行用时    |
| -------------- | ------------- | ---------- | ----------- |
| Ans 1 (Python) | $O(26×N^3×M)$ | $O(N)$     | 636ms (54%) |
| Ans 2 (Python) |               |            |             |
| Ans 3 (Python) |               |            |             |

解法一：

```python
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        def check(s1, s2):
            num = 0
            for ii in range(len(s1)):
                if s1[ii] != s2[ii]:
                    num += 1
                    if num >= 2:
                        return False
            return num == 1

        ans = 0
        for length in range(1, len(s) + 1):
            cache = {}
            for i in range(len(s) - length + 1):
                # 获取当前字符串
                pattern = s[i:i + length]

                # 如果没被计算过，则遍历t计算
                if pattern not in cache:
                    num = 0
                    for j in range(len(t) - length + 1):
                        if check(pattern, t[j:j + length]):
                            num += 1
                    cache[pattern] = num

                # 累加当前结果到答案
                # print(pattern, ":", cache[pattern])
                ans += cache[pattern]

        return ans
```