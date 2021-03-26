# LeetCode题解(0898)：子数组按位或操作(Python)

题目：[原题链接](https://leetcode-cn.com/problems/bitwise-ors-of-subarrays/)（中等）

标签：位运算、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(NlogN)$ | 752ms (69.35%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans = set()
        now = {0}
        for x in A:
            now = {x | y for y in now} | {x}
            ans |= now
        return len(ans)
```

