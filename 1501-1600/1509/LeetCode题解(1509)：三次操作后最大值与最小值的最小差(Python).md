# LeetCode题解(1509)：三次操作后最大值与最小值的最小差(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/)（中等）

标签：数组、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 80ms (99%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # 处理长度小于4的情况
        if len(nums) <= 4:
            return 0

        # 4个最小值和4个最大值
        min_val = list(sorted(nums[:4]))  # 从小到大
        max_val = min_val[::-1]  # 从大到小

        # 遍历数组寻找4个最小值和4个最大值
        for i in range(4, len(nums)):
            num = nums[i]
            if num < min_val[-1]:
                min_val.pop()
                min_val.append(num)
                min_val.sort()

            if num > max_val[-1]:
                max_val.pop()
                max_val.append(num)
                max_val.sort(reverse=True)

        # 处理4种可能的删除方法
        return min(max_val[i] - min_val[3 - i] for i in range(4))
```