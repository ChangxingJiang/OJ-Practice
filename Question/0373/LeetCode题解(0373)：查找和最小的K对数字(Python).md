# LeetCode题解(0373)：查找和最小的K对数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums/)（中等）

标签：堆、动态规划

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时       |
| -------------- | ------------ | ---------- | -------------- |
| Ans 1 (Python) | $O(K×N1)$    | $O(N1)$    | 220ms (40.35%) |
| Ans 2 (Python) | $O(K×logN1)$ | $O(N1)$    | 60ms (85.75%)  |
| Ans 3 (Python) |              |            |                |

解法一：

```python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        size1, size2 = len(nums1), len(nums2)
        dp = [0] * size1  # 左侧每个数字匹配到的位置

        ans = []
        for _ in range(min(size1 * size2, k)):
            min_i1, min_val = -1, float("inf")
            for i1 in range(size1):
                i2 = dp[i1]
                if i2 < size2:
                    val = nums1[i1] + nums2[i2]
                    if val < min_val:
                        min_i1, min_val = i1, val

            ans.append([nums1[min_i1], nums2[dp[min_i1]]])
            dp[min_i1] += 1

        return ans
```

解法二（堆）：

```python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        size1, size2 = len(nums1), len(nums2)
        heap = [(nums2[0] + nums1[i], i, 0) for i in range(size1)]

        ans = []
        for _ in range(min(size1 * size2, k)):
            val, i1, i2 = heapq.heappop(heap)
            ans.append([nums1[i1], nums2[i2]])
            if i2 < size2 - 1:
                heapq.heappush(heap,(nums1[i1] + nums2[i2 + 1], i1, i2 + 1))

        return ans
```