# LeetCode题解(0330)：按要求补齐数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/patching-array/)（困难）

标签：贪心算法

| 解法           | 时间复杂度  | 空间复杂度 | 执行用时      |
| -------------- | ----------- | ---------- | ------------- |
| Ans 1 (Python) | $O(M+logN)$ | $O(1)$     | 64ms (98.65%) |
| Ans 2 (Python) |             |            |               |
| Ans 3 (Python) |             |            |               |

解法一：

```python
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # 处理数组为空的情况
        if not nums:
            ans = 0
            total = 0
            while total < n:
                total += (total + 1)
                ans += 1
            return ans

        # 处理数组不为空的情况
        else:
            ans = 0

            # 处理第1个数之前的情况
            total = 0
            while total < nums[0] - 1:
                total += (total + 1)
                ans += 1

            total += nums[0]
            # 处理数组中间的数
            for i in range(1, len(nums)):
                if nums[i] > n:
                    break
                while total < nums[i] - 1:
                    total += (total + 1)
                    ans += 1
                total += nums[i]

            # 处理最后1个数之后的情况
            while total < n:
                total += (total + 1)
                ans += 1

            return ans
```

