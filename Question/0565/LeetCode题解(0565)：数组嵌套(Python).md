# LeetCode题解(0565)：数组嵌套(Python)

题目：[原题链接](https://leetcode-cn.com/problems/array-nesting/)（中等）

标签：动态规划、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 172ms (16.33%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        size = len(nums)

        dp = [0] * size
        for i in range(size):
            if dp[i] != 0:
                continue

            count = {}
            lst = []
            while i not in count and dp[i] == 0:
                count[i] = len(lst)
                lst.append(i)
                i = nums[i]

            # 遇到之前已经遍历的情况
            if dp[i] != 0:
                now = dp[i] + 1
                while lst:
                    dp[lst.pop()] = now
                    now += 1

            # 之前尚未遍历的情况，即进入循环的情况
            circle = len(lst) - count[i]  # 循环节长度
            for j in range(len(lst)):
                if j < count[i]:
                    dp[lst[j]] = len(lst) - j
                else:
                    dp[lst[j]] = circle

        return max(dp)
```

