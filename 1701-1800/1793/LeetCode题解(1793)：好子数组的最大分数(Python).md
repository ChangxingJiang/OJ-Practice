# LeetCode题解(1793)：好子数组的最大分数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-score-of-a-good-subarray/)（困难）

标签：贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 232ms (80.30%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        size = len(nums)

        i, j = k, k  # 当前左右位置
        now = nums[k]  # 当前最小值

        # 寻找左侧或右侧大于当前最小值的值
        while i > 0 and nums[i - 1] >= now:
            i -= 1
        while j < size - 1 and nums[j + 1] >= now:
            j += 1

        ans = now * (j - i + 1)

        while i > 0 or j < size - 1:
            # 选择左右侧相对大的一个值使当前最小值变小
            if i > 0 and j < size - 1:
                if nums[i - 1] < nums[j + 1]:
                    now = nums[j + 1]
                    j += 1
                else:
                    now = nums[i - 1]
                    i -= 1
            elif i > 0:
                now = nums[i - 1]
                i -= 1
            elif j < size - 1:
                now = nums[j + 1]
                j += 1

            # 寻找左侧或右侧大于当前最小值的值
            while i > 0 and nums[i - 1] >= now:
                i -= 1
            while j < size - 1 and nums[j + 1] >= now:
                j += 1

            ans = max(ans, now * (j - i + 1))

        return ans
```

