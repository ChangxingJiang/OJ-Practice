# LeetCode题解(0324)：摆动排序II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/wiggle-sort-ii/)（中等）

标签：排序、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 1992ms (19.20%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        size = len(nums)

        # 处理特殊情况
        if size <= 1:
            return

        # 快速排序中的快速选择算法找到中位数
        def partition(begin, end):
            l, r = begin, end
            while l < r:
                while l < r and nums[l] < nums[r]:
                    r -= 1
                if l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                while l < r and nums[l] < nums[r]:
                    l += 1
                if l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    r -= 1
            return l

        mid = (size - 1) // 2  # 中位数索引

        # 执行快速排序中的快速选择算法找到中位数
        left, right = 0, size - 1
        while True:
            pivot = partition(left, right)
            # print("快速排序:", nums, nums[pivot], [pivot])
            if pivot == mid:
                break
            elif pivot > mid:
                right = pivot - 1
            else:
                left = pivot + 1

        # 三路划分：使中位数位于数组中间，小于中位数的数放在左边，大于中位数的数放在右边
        mid_val = nums[mid]
        left, curr, right = 0, 0, size - 1
        while curr < right:
            if nums[curr] < mid_val:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] > mid_val:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            else:
                curr += 1

        # 交叉合并（原地-未实现）
        # mid += 1
        # j = mid
        # for i in range(1, len(nums)):
        #     if i % 2 == 1:
        #         nums[i], nums[j] = nums[j], nums[i]
        #     else:
        #         if i < mid:
        #             nums[i], nums[mid] = nums[mid], nums[i]
        #         j += 1
        #
        # if len(nums) % 2 == 0:
        #     for i in range(1, len(nums), 2):
        #         nums[i - 1], nums[i] = nums[i], nums[i - 1]
        # nums.reverse()

        # 较差合并（非原地）
        small, big, _nums = mid, size - 1, nums[:]
        for i in range(size):
            if i % 2 == 0:
                nums[i] = _nums[small]
                small -= 1
            else:
                nums[i] = _nums[big]
                big -= 1
```

