# LeetCode题解(1835)：所有数对按位与结果的异或和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-xor-sum-of-all-pairs-bitwise-and/)（困难）

标签：位运算、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 128ms (43.95%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        s1, s2 = len(arr1), len(arr2)

        ans1 = 0
        ans2 = 0

        for i in range(s1):
            ans1 ^= arr1[i]

        for i in range(s2):
            ans2 ^= arr2[i]

        return ans1 & ans2
```

