# LeetCode题解(1685)：有序数组中差绝对值之和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sum-of-absolute-differences-in-a-sorted-array/)（中等）

标签：数组、数学、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 332ms (11.99%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # 计算各位之间的差
        lst = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]

        # 计算前缀值和后缀值
        pre1 = [(i + 1) * lst[i] for i in range(len(lst))]
        suf1 = [(len(lst) - i) * lst[i] for i in range(len(lst))]

        # 计算前缀积的前缀值、后缀值的后缀和
        now = 0
        pre2 = [0]
        for i in range(len(pre1)):
            now += pre1[i]
            pre2.append(now)
        now = 0
        suf2 = [0]
        for i in range(len(suf1) - 1, -1, -1):
            now += suf1[i]
            suf2.append(now)
        suf2.reverse()

        # 计算最终结果
        ans = []
        for i in range(len(nums)):
            ans.append(pre2[i] + suf2[i])
        return ans
```

