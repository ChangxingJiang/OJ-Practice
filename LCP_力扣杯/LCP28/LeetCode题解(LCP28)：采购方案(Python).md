# LeetCode题解(LCP28)：采购方案(Python)

题目：[原题链接](https://leetcode-cn.com/problems/4xy4Wx/)（简单）

标签：排序、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 400ms (20.43%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
import bisect


class Solution:
    _MOD = 1000000007

    def purchasePlans(self, nums: List[int], target: int) -> int:
        size = len(nums)

        nums.sort()

        ans = 0

        for i in range(size):
            j = bisect.bisect_right(nums, target - nums[i])
            if j > i:
                ans += (j - i - 1)

        return ans % self._MOD
```

