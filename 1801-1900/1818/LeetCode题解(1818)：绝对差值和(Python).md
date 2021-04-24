# LeetCode题解(1818)：绝对差值和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-absolute-sum-difference/)（中等）

标签：贪心算法、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 448ms (66.23%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
import bisect


class Solution:
    _MOD = 10 ** 9 + 7

    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        array1 = list(sorted(nums1))

        ans = 0  # 绝对差值和
        most = 0  # 最大可缩小值
        for i in range(n):
            n1, n2 = nums1[i], nums2[i]
            diff = abs(n2 - n1)

            ans += diff

            maybe = 0
            j = bisect.bisect_right(array1, n2)
            # print(array1, n2, j)
            if j > 0:
                diff1 = abs(n2 - array1[j - 1])
                maybe = max(maybe, diff - diff1)
            if j < n:
                diff2 = abs(n2 - array1[j])
                maybe = max(maybe, diff - diff2)

            most = max(most, maybe)

        # print(ans, most)

        return (ans - most) % self._MOD
```

