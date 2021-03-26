# LeetCode题解(0321)：拼接最大数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/create-maximum-number/)（困难）

标签：贪心算法、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×K^2)$ | $O(N)$     | 248ms (88.77%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # 选取每个数组中最大的子序列
        def pick_max(nums, k):
            stack = []
            drop = len(nums) - k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        # 合并两个数组的最大子序列
        def merge(A, B):
            lst = []
            while A or B:
                bigger = A if A > B else B
                lst.append(bigger[0])
                bigger.pop(0)
            return lst

        return max(merge(pick_max(nums1, i), pick_max(nums2, k - i)) for i in range(k + 1) if
                   i <= len(nums1) and k - i <= len(nums2))
```