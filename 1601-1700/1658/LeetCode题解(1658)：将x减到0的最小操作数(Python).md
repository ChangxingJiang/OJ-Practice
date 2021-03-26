# LeetCode题解(1658)：将x减到0的最小操作数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-operations-to-reduce-x-to-zero/)（中等）

标签：贪心算法、双指针、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 544ms (29.16%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 寻找处理方案
        last = 0
        count_left = {0: 0}
        for i, n in enumerate(nums):
            last += n
            count_left[last] = i + 1

        # print(count_left)

        choose = []

        last = 0
        for i, n in enumerate(nums[::-1]):
            aim = x - last
            if aim in count_left:
                if count_left[aim] + i <= len(nums):
                    choose.append((count_left[aim], i))
            last += n

        # 寻找操作数最少的处理方案
        if not choose:
            return -1
        choose.sort(key=lambda k: k[0] + k[1])

        # print(choose)

        # 处理字符串并返回结果
        ans = choose[0]

        nums[:] = nums[ans[0]:-ans[1]]

        # print(nums)

        return ans[0] + ans[1]
```

