# LeetCode题解(1775)：通过最少操作次数使数组的和相等(Python)

题目：[原题链接](https://leetcode-cn.com/problems/equal-sum-arrays-with-minimum-number-of-operations/)（中等）

标签：贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N1+N2)$ | $O(6)$     | 108ms (93.17%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        c1, c2 = collections.Counter(nums1), collections.Counter(nums2)
        s1, s2 = sum(i * c1[i] for i in range(1, 7)), sum(i * c2[i] for i in range(1, 7))

        if s1 == s2:
            return 0

        if s1 > s2:
            s1, s2 = s2, s1
            c1, c2 = c2, c1

        # s1 < s2

        diff = s2 - s1
        ans = 0

        if c1[1] > 0 or c2[6] > 0:
            if (c1[1] + c2[6]) * 5 >= diff:
                return ans + math.ceil(diff / 5)
            else:
                diff -= (c1[1] + c2[6]) * 5
                ans += (c1[1] + c2[6])

        if c1[2] > 0 or c2[5] > 0:
            if (c1[2] + c2[5]) * 4 >= diff:
                return ans + math.ceil(diff / 4)
            else:
                diff -= (c1[2] + c2[5]) * 4
                ans += (c1[2] + c2[5])

        if c1[3] > 0 or c2[4] > 0:
            if (c1[3] + c2[4]) * 3 >= diff:
                return ans + math.ceil(diff / 3)
            else:
                diff -= (c1[3] + c2[4]) * 3
                ans += (c1[3] + c2[4])

        if c1[4] > 0 or c2[3] > 0:
            if (c1[4] + c2[3]) * 2 >= diff:
                return ans + math.ceil(diff / 2)
            else:
                diff -= (c1[4] + c2[3]) * 2
                ans += (c1[4] + c2[3])

        if c1[5] > 0 or c2[2] > 0:
            if (c1[5] + c2[2]) * 1 >= diff:
                return ans + math.ceil(diff / 1)
            else:
                diff -= (c1[5] + c2[2]) * 1
                ans += (c1[5] + c2[2])

        return -1
```

