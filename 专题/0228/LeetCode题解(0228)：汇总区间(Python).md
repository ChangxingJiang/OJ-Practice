# LeetCode题解(0228)：汇总区间(Python)

题目：[原题链接](https://leetcode-cn.com/problems/summary-ranges/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (77.80%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        now = nums[0]
        last = nums[0]

        ans = []

        for i in range(1, len(nums)):
            if nums[i] != last + 1:
                ans.append(str(now) + "->" + str(last) if now != last else str(now))
                now = last = nums[i]
            else:
                last += 1

        ans.append(str(now) + "->" + str(last) if now != last else str(now))

        return ans
```