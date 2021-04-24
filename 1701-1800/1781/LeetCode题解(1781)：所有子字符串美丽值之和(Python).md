# LeetCode题解(1781)：所有子字符串美丽值之和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sum-of-beauty-of-all-substrings/)（中等）

标签：哈希表、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(26)$    | 4580ms (27.34%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0

        size = len(s)
        for i in range(size):
            fre_list = [0] * 26
            for j in range(i, size):
                idx = ord(s[j]) - 97
                fre_list[idx] += 1
                ans += max(fre_list) - min(fre for fre in fre_list if fre > 0)

        return ans
```

