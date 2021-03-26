# LeetCode题解(1498)：满足条件的子序列数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)（中等）

标签：排序、二分查找、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 8068ms (44%) |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

解法一：

```python
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        ans = 0

        for i in range(len(nums)):
            val = nums[i]
            idx = bisect.bisect_right(nums, target - val)

            if idx > i:
                ans += 2 ** (idx - i - 1)

            # print(i, "->", idx, "(", target - val, ")")

        return ans % (10 ** 9 + 7)
```