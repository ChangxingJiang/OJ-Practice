# LeetCode题解(0719)：找出第k小的距离对(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-k-th-smallest-pair-distance/)（困难）

标签：堆、二分查找、数组

| 解法           | 时间复杂度                                         | 空间复杂度 | 执行用时       |
| -------------- | -------------------------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN+KlogN)$                                   | $O(N)$     | 超出时间限制   |
| Ans 2 (Python) | $O(NlogN+NlogW)$ : 其中W为nums中最大值与最小值的差 | $O(N)$     | 128ms (91.36%) |
| Ans 3 (Python) |                                                    |            |                |

解法一（堆）：

```python
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # 排序列表
        # O(NlogN)
        nums.sort()

        # 定义从每个位置开始累加的距离之和的堆
        # O(N)
        heap = [(nums[i + 1] - nums[i], i, i + 1) for i in range(len(nums) - 1)]
        heapq.heapify(heap)

        # 生成第K个绝对差值（使第K个绝对差值成为堆顶）
        # O(KlogN)
        for j in range(k - 1):
            distance, i1, i2 = heapq.heappop(heap)
            if i2 + 1 < len(nums):
                heapq.heappush(heap, (nums[i2 + 1] - nums[i1], i1, i2 + 1))

        # 返回第K个绝对差值
        return heapq.heappop(heap)[0]
```

解法二（二分查找）：

```python
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # 滑动窗口判断有多少符合要求的差值
        # 每次: O(N)
        def count(guess):
            total = 0
            l = 0
            for r in range(1, len(nums)):
                while l < r and nums[r] - nums[l] > guess:
                    l += 1
                total += r - l
            # print(guess, "->", total)
            return total

        # 排序列表
        # O(NlogN)
        nums.sort()

        # 二分查找寻找目标值
        # O(NlogW) 其中W为nums中最大值与最小值的差
        ans = 0
        left, right = 0, nums[-1] - nums[0]
        while left <= right:
            mid = (left + right) // 2
            # print(left, right, "->", mid)
            if count(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
```